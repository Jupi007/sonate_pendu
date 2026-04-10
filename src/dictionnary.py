class _Dictionnary:
    def __init__(self):
        with open("src/data/dictionnaire.txt", "r") as file:
            self._words = [line.split(";")[0].strip() for line in file if line.strip()]

    @property
    def len(self):
        return len(self._words)

    def get(self, id):
        return self._words[id]


dictionnary = _Dictionnary()
