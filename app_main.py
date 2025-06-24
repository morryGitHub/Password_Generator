import asyncio
import os

import logging

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot
from handlers.last_command import process_last_pending_update
from handlers.user_message import user_message
from handlers.user_callback import user_callback
from keyboards.botCommands import set_bot_commands


async def main():
    load_dotenv()
    bot = Bot(os.getenv("API_TOKEN"))

    await set_bot_commands(bot)

    dp = Dispatcher()
    dp.include_router(user_callback)
    dp.include_router(user_message)

    await process_last_pending_update(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print("Bot is running")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
