import asyncio
import datetime as dt

import requests
import telegram

from constants import ALPHAVANTAGE_API_KEY, CHATID_W, NEWS_API, TELEGRAM_TOKEN

ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


tickers = [("AAPL", "Apple"), ("TSLA", "Tesla")]


def make_call(symbol):
    payload = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": ALPHAVANTAGE_API_KEY,
    }
    r = requests.get(ALPHAVANTAGE_ENDPOINT, params=payload)
    r.raise_for_status()
    return r.json()["Time Series (Daily)"]


def price_fluctuation(json_data):
    current_date = dt.datetime.today()
    prices = []
    i = 0
    while len(prices) < 2:
        try:
            price = json_data[(current_date - dt.timedelta(days=(i))).isoformat()[:10]][
                "1. open"
            ]
            prices.append(float(price))
        except KeyError:
            pass
        finally:
            i += 1
    prev_date = (current_date - dt.timedelta(days=(i))).isoformat()
    prev_open, latest_open = prices[1], prices[0]
    if latest_open > prev_open:  # prices have gone up
        return (
            latest_open,
            ((latest_open / prev_open) - 1) * 100,
            (current_date - dt.timedelta(days=(i))).isoformat()[:10],
        )
    elif latest_open < prev_open:  # prices have come down
        return (
            latest_open,
            -((prev_open - latest_open) / prev_open) * 100,
            (current_date - dt.timedelta(days=(i))).isoformat()[:10],
        )
    else:
        return 0


async def tbot(msg):
    bot = telegram.Bot(TELEGRAM_TOKEN)
    async with bot:
        await bot.send_message(
            text=msg,
            chat_id=CHATID_W,
        )


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get
#  the first 3 news pieces for the COMPANY_NAME.


def get_news(ticker, date):
    payload = {
        "q": ticker,
        "from": date,
        "to": dt.datetime.today().isoformat(),
        "searchIn": "title",
        "language": "en",
        "sortBy": "relevancy",
        "apiKey": NEWS_API,
    }
    r = requests.get(NEWS_ENDPOINT, params=payload)
    r.raise_for_status()
    return r.json()["articles"]


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage
#  change and each article's title and description to your phone number.


def notify(symbol, company_name, price, movement, news):
    if movement > 0:
        message = f"{symbol}: ${price} (🔺{movement:.02f}%)"
    else:
        message = f"{symbol}: ${price} (🔻{abs(movement):.02f}%)"
    for article in news[:3]:
        message += f"\n\nHeadline: {article['title']}\nBrief: {article['description']}"
    asyncio.run(tbot(message))


for symbol, company_name in tickers:
    price, movement, date = price_fluctuation(make_call(symbol))
    if not movement:
        pass
    else:
        news = get_news(company_name, date)
        notify(symbol, company_name, price, movement, news)

# Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F
#  filings that hedge funds and prominent investors are required
#   to file by the SEC The 13F filings show the
#    funds' and investors' portfolio positions as
#     of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over
#  821 13F filings that hedge funds and prominent investors
#   are required to file by the SEC The 13F
#    filings show the funds' and investors' portfolio
#     positions as of March 31st, near the height of the coronavirus market crash.
# """
