from flask import session

from src.game.game_state import UNDEFINED_WORD_ID, GameState


_USERNAME_SESSION_KEY = "username"
_WORD_ID_SESSION_KEY = "word_id"
_PLAYER_ATTEMPTS_SESSION_KEY = "player_attempts"


class _SessionGameState(GameState):
    @property
    def username(self) -> str:
        return session.get(_USERNAME_SESSION_KEY, "")

    @username.setter
    def username(self, value: str):
        session[_USERNAME_SESSION_KEY] = value

    @property
    def word_id(self) -> int:
        return int(session.get(_WORD_ID_SESSION_KEY, UNDEFINED_WORD_ID))

    @word_id.setter
    def word_id(self, value: int):
        session[_WORD_ID_SESSION_KEY] = value

    @property
    def player_attempts(self) -> list[str]:
        return list(session.get(_PLAYER_ATTEMPTS_SESSION_KEY, ""))

    @player_attempts.setter
    def player_attempts(self, value: list[str]):
        session[_PLAYER_ATTEMPTS_SESSION_KEY] = "".join(value)

    def clear(self):
        session.clear()


session_game_state = _SessionGameState()
