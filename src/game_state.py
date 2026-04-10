from flask import session


_USERNAME_SESSION_KEY = "username"
_WORD_ID_SESSION_KEY = "word_id"
_PLAYER_ATTEMPTS_SESSION_KEY = "player_attempts"


class _GameState:
    @property
    def username(self):
        return session.get(_USERNAME_SESSION_KEY, '')

    @username.setter
    def username(self, value):
        session[_USERNAME_SESSION_KEY] = value

    @property
    def word_id(self):
        return session.get(_WORD_ID_SESSION_KEY, None)

    @word_id.setter
    def word_id(self, value):
        session[_WORD_ID_SESSION_KEY] = value

    @property
    def player_attempts(self):
        return list(session.get(_PLAYER_ATTEMPTS_SESSION_KEY, ""))

    def add_player_attempt(self, letter):
        assert len(letter) == 1
        player_attempts = self.player_attempts
        letter = letter.upper()

        if not letter in player_attempts:
            player_attempts += letter
            session[_PLAYER_ATTEMPTS_SESSION_KEY] = "".join(player_attempts)

    def clear(self):
        session.clear()


game_state = _GameState()
