from flask import session

_USERNAME_SESSION_KEY = "username"
_WORD_ID_SESSION_KEY = "word_id"


class _GameState:
    @property
    def username(self):
        return session.get(_USERNAME_SESSION_KEY)

    @username.setter
    def username(self, value):
        session[_USERNAME_SESSION_KEY] = value

    @property
    def word_id(self):
        return session.get(_WORD_ID_SESSION_KEY)

    @word_id.setter
    def word_id(self, value):
        session[_WORD_ID_SESSION_KEY] = value

    def clear(self):
        session.clear()


game_state = _GameState()
