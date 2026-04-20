from src.game.dictionnary import dictionnary
from src.game.game_state import GameState

PLAYER_LIFES = 5


class HangmanGame:
    def __init__(self, state: GameState):
        self._state = state

    @property
    def remaining_lifes(self) -> int:
        word = dictionnary.get(self._state.word_id)
        remaining_lifes = PLAYER_LIFES
        for letter in self._state.player_attempts:
            if not letter in word:
                remaining_lifes -= 1
        return remaining_lifes

    @property
    def hint(self) -> str:
        word = dictionnary.get(self._state.word_id)
        hint = ""
        for letter in word:
            if letter in self._state.player_attempts:
                hint += letter
            else:
                hint += "_"
        return hint

    def remaining_word_letters(self) -> int:
        word = dictionnary.get(self._state.word_id)
        remaining_word_letters = list(set(word))
        for letter in self._state.player_attempts:
            if letter in remaining_word_letters:
                remaining_word_letters.remove(letter)
        return len(remaining_word_letters)

    def attempt(self, letter: str) -> None:
        assert len(letter) == 1
        player_attempts = self._state.player_attempts
        letter = letter.upper()

        if not letter in player_attempts:
            player_attempts += letter
            self._state.player_attempts = player_attempts
