from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from aiogram import Router, F, Bot
from keyboards.user_kb import custom_password_kb
from services.FSMState import messages

user_callback = Router()


@user_callback.callback_query(F.data.startswith("change_"))
async def on_change_setting(callback: CallbackQuery, state: FSMContext, bot: Bot):
    user_id = callback.from_user.id

    data = callback.data.strip().split("_")
    info = data[1]
    change = data[2]

    state_data = await state.get_data()
    if info == "word":
        current_count = state_data.get("word_count", 4)
        try:
            new_count = current_count + int(change)
            if new_count < 2:
                await callback.answer("Меньше чем 2 слова - нельзя")
                return
            new_count = max(2, new_count)  # не меньше 1
        except ValueError:
            new_count = current_count
        await state.update_data(word_count=new_count)

    elif info == "prefixes":
        prefixes = state_data.get("prefixes", False)
        await state.update_data(prefixes=not prefixes)

    elif info == "separators":
        separators = state_data.get("separators", True)
        await state.update_data(separators=not separators)

    await callback.answer("")

    state_data = await state.get_data()
    if callback.from_user.id in messages:
        message_id = messages.get(user_id)
    keyboard, _ = custom_password_kb(state_data.get("word_count", 4), state_data.get("prefixes", False),
                                     state_data.get("separators", True))

    try:
        await bot.edit_message_text(
            chat_id=callback.message.chat.id,
            text="Ваши настройки: \n"
                 f"<b>Количество слов</b>: {state_data.get("word_count", 4)}\n"
                 f"<b>Префиксы\суффиксы</b>: {'Да' if state_data.get("prefixes", False) else 'Нет'}\n"
                 f"<b>Разделители между словами</b>: {'Да' if state_data.get("separators", True) else 'Нет'}\n\n"
                 "Используйте кнопки ниже для изменения настроек.\n"
                 r"Затем вызовите команду /generate для генерации пароля с этими настройками.",
            message_id=message_id.message_id,
            reply_markup=keyboard,
            parse_mode=ParseMode.HTML
        )
    except TelegramBadRequest:
        pass
