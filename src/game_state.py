from flask import session

_USERNAME_KEY = "username"
_WORD_ID_KEY = "word_id"


class _GameState:
    @property
    def username(self):
        return session.get(_USERNAME_KEY)

    @username.setter
    def username(self, value):
        session[_USERNAME_KEY] = value


game_state = _GameState()
