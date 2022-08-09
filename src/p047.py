# Amazon price tracker

import lxml
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B087LXCTFJ/"

hdrs = {
    "Accept-Language": "en-GB,en;q=0.5",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; "
        "Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
    ),
}

r = requests.get(url, headers=hdrs)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
price = float(
    f"{soup.select('span.a-price-whole')[0].text}"
    f"{soup.select('span.a-price-fraction')[0].text}"
)
print(price)
