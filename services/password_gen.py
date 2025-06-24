from random import choice

from xkcdpass import xkcd_password as xp
from string import ascii_lowercase as chars_lower


class XKCD:
    delimiters_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    delimiters_full = ["!", "$", "%", "&", "*", "-", "_", "+", "=", ":", "~", "?", "/", ";"] + delimiters_numbers
    word_file = xp.locate_wordfile()

    def __init__(self):
        self.word_list = xp.generate_wordlist(
            wordfile=self.word_file,
            min_length=4,
            max_length=8,
            valid_chars='[a-z]'
        )

    def weak(self):
        """Слабый пароль: 2 слова без разделителей"""
        return xp.generate_xkcdpassword(
            wordlist=self.word_list,
            numwords=2,
            delimiter="-",
        )

    def normal(self):
        """Средний пароль: 3 слова, разделитель в виде случайной цифры"""
        return xp.generate_xkcdpassword(
            wordlist=self.word_list,
            numwords=3,
            valid_delimiters=self.delimiters_full,
            random_delimiters=True,
            case="random"
        )

    def strong(self):
        """Сильный пароль: 4 слова и большой выбор разделителей"""
        return xp.generate_xkcdpassword(
            wordlist=self.word_list,
            numwords=4,
            valid_delimiters=self.delimiters_full,
            random_delimiters=True,
            case="random"
        )

    def custom(self,
               count: id,
               separators: bool,
               prefixes: bool):
        """Произвольный пароль: сложность зависит от настроек пользователя"""
        pwd = xp.generate_xkcdpassword(
            wordlist=self.word_list,
            numwords=count,
            delimiter="",
            valid_delimiters=self.delimiters_full,
            random_delimiters=separators,
            case="random"
        )

        if prefixes == separators:
            return pwd
        elif separators and not prefixes:
            return pwd[1:-1]
        elif prefixes and not separators:
            return f"{choice(self.delimiters_full)}{pwd}{choice(self.delimiters_full)}"


xkcd = XKCD()
