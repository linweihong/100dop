import asyncio

import telegram

from constants import CHATID_W, TELEGRAM_TOKEN


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.bot = telegram.Bot(TELEGRAM_TOKEN)

    def notify(self, message):
        asyncio.run(self.send_message(message))

    async def send_message(self, message):
        async with self.bot:
            await self.bot.send_message(text=message, chat_id=CHATID_W)
