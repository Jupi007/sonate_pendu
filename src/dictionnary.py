import random

from unidecode import unidecode


class _Dictionnary:
    def __init__(self):
        with open("src/data/dictionnaire.txt", "r") as file:
            self._words = [self._normalize_line(line) for line in file if line.strip()]

    def _normalize_line(self, line: str):
        # Remove accented characters with unidecode
        return unidecode(line.split(";")[0].strip()).upper()

    def get_random_word_id(self) -> int:
        return random.randint(0, len(self._words))

    def get(self, id: int) -> str:
        return self._words[id]


dictionnary = _Dictionnary()
