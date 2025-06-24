from uuid import uuid4

from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from aiogram import Router, Bot
from services.password_gen import xkcd

user_inline = Router()


# todo try to do smth interesting with this
@user_inline.inline_query()
async def inline_generate_normal(inline_query: InlineQuery, bot: Bot):
    pwd = xkcd.normal()

    result = InlineQueryResultArticle(
        id=str(uuid4()),
        title="Сгенерировать обычный пароль",
        description="Генерация нормального пароля через inline",
        input_message_content=InputTextMessageContent(
            message_text=f"`{pwd}`",
            parse_mode="MarkdownV2"
        )
    )

    await bot.answer_inline_query(
        inline_query.id,
        results=[result],
        cache_time=0
    )
