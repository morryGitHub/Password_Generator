from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router
from keyboards.user_kb import custom_password_kb
from services.password_gen import xkcd
from services.FSMState import messages

user_message = Router()


@user_message.message(CommandStart())
async def start_handler(message: Message):
    await message.answer('''Привет! Я — бот для генерации паролей. Вот что я умею:

• /generate_weak — создать простой пароль
• /generate_normal — создать пароль средней сложности
• /generate_strong — создать сильный и сложный пароль
• /settings — настроить параметры генерации (количество слов, префиксы, разделители)
• /generate — сгенерировать пароль по текущим настройкам

Используй команды, чтобы получить нужный пароль быстро и удобно! Если хочешь, могу помочь с настройками — вызывай /settings.''')


@user_message.message(Command("generate_weak"))
async def cmd_generate_weak(message: Message):
    pwd: xkcd = xkcd.weak()
    await message.answer(f"`{pwd}`", parse_mode=ParseMode.MARKDOWN_V2)


@user_message.message(Command("generate_normal"))
async def cmd_generate_normal(message: Message):
    pwd: xkcd = xkcd.normal()
    await message.answer(f"`{pwd}`", parse_mode=ParseMode.MARKDOWN_V2)


@user_message.message(Command("generate_strong"))
async def cmd_generate_strong(message: Message):
    pwd: xkcd = xkcd.strong()
    await message.answer(f"`{pwd}`", parse_mode=ParseMode.MARKDOWN_V2)


@user_message.message(Command("settings"))
async def cmd_generate_custom(message: Message, state: FSMContext):
    data = await state.get_data()
    word = data.get("word_count", 4)
    prefixes = data.get("prefixes", False)
    separators = data.get("separators", True)
    keyboard, custom_text = custom_password_kb(word, prefixes, separators)
    message_id = await message.answer(custom_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)
    messages[message.from_user.id] = message_id


@user_message.message(Command("generate"))
async def cmd_generate(message: Message, state: FSMContext):
    state_data = await state.get_data()
    word_count = state_data.get("word_count", 4)
    prefixes = state_data.get("prefixes", False)
    separators = state_data.get("separators", True)
    pwd: xkcd = xkcd.custom(
        count=word_count,
        prefixes=prefixes,
        separators=separators,
    )
    await message.answer(f"`{pwd}`", parse_mode=ParseMode.MARKDOWN_V2)
