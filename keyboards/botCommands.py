from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="generate_weak", description="Генерировать слабый пароль"),
        BotCommand(command="generate_normal", description="Генерировать нормальный пароль"),
        BotCommand(command="generate_strong", description="Генерировать сильный пароль"),
        BotCommand(command="settings", description="Настройки пароля"),
        BotCommand(command="generate", description="Генерировать пароль с настройками"),
    ]
    await bot.set_my_commands(commands)
