from src.constants import PLAYER_LIFES


class Gallows:
    _STAGES = [
        """
   +---+
       |
       |
       |
       |
       |
=========
""",
        """
   +---+
   |   |
       |
       |
       |
       |
=========
""",
        """
   +---+
   |   |
   O   |
       |
       |
       |
=========
""",
        """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
""",
        """
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
""",
        """
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
""",
    ]

    def get_progress_ascii(remaining_lifes):
        return Gallows._STAGES[PLAYER_LIFES - remaining_lifes]
