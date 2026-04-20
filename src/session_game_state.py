from flask import session


_USERNAME_SESSION_KEY = "username"
_WORD_ID_SESSION_KEY = "word_id"
_PLAYER_ATTEMPTS_SESSION_KEY = "player_attempts"


class _SessionGameState:
    @property
    def username(self) -> str:
        return session.get(_USERNAME_SESSION_KEY, "")

    @username.setter
    def username(self, value: str):
        session[_USERNAME_SESSION_KEY] = value

    @property
    def word_id(self) -> int:
        return int(session.get(_WORD_ID_SESSION_KEY, None))

    @word_id.setter
    def word_id(self, value: int):
        session[_WORD_ID_SESSION_KEY] = value

    @property
    def player_attempts(self) -> list[str]:
        return list(session.get(_PLAYER_ATTEMPTS_SESSION_KEY, ""))

    def add_player_attempt(self, letter: str):
        assert len(letter) == 1
        player_attempts = self.player_attempts
        letter = letter.upper()

        if not letter in player_attempts:
            player_attempts += letter
            session[_PLAYER_ATTEMPTS_SESSION_KEY] = "".join(player_attempts)

    def clear(self):
        session.clear()


session_game_state = _SessionGameState()
