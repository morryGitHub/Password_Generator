from aiogram.types import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton


def custom_password_kb(word: int, prefixes: int, separators: int):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='-слово', callback_data=f"change_word_-1"),
            InlineKeyboardButton(text='+слово', callback_data=f"change_word_1")],
        [
            InlineKeyboardButton(text='Добавить префикс и суффикс', callback_data=f"change_prefixes_0")
        ],
        [
            InlineKeyboardButton(text='Убрать разделители', callback_data=f"change_separators_0")
        ]
    ])
    return keyboard, ("Ваши настройки: \n"
                      f"<b>Количество слов</b>: {word}\n"
                      f"<b>Префиксы\суффиксы</b>: {'Да' if prefixes else 'Нет'}\n"
                      f"<b>Разделители между словами</b>: {'Да' if separators else 'Нет'}\n\n"
                      "Используйте кнопки ниже для изменения настроек.\n"
                      r"Затем вызовите команду /generate для генерации пароля с этими настройками.")
