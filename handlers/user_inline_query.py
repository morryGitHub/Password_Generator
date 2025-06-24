from uuid import uuid4

from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from aiogram import Router, F, Bot
from keyboards.user_kb import custom_password_kb
from services.FSMState import messages

user_inline = Router()


# todo try to do smth interesting with this
@user_inline.inline_query()
async def inline_echo_handler(inline_query: InlineQuery, bot: Bot):
    user_input = inline_query.query or "Пусто"

    result = InlineQueryResultArticle(
        id=str(uuid4()),
        title=f"Эхо: {user_input}",
        description="Нажми, чтобы отправить этот текст",
        input_message_content=InputTextMessageContent(
            message_text=f"🔁 Ты написал: <b>{user_input}</b>",
            parse_mode="HTML"
        )
    )

    await bot.answer_inline_query(
        inline_query.id,
        results=[result],
        cache_time=1  # 1 секунда — без кэша
    )
