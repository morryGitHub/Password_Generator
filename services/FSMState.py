from aiogram.fsm.state import StatesGroup, State


class SettingsStates(StatesGroup):
    word_count = State()
    prefixes = State()
    separators = State()


messages = {}
