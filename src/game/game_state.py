from abc import ABC, abstractmethod


UNDEFINED_WORD_ID = -1


class GameState(ABC):
    @property
    @abstractmethod
    def username(self) -> str:
        pass

    @username.setter
    @abstractmethod
    def username(self, value: str) -> None:
        pass

    @property
    @abstractmethod
    def word_id(self) -> int:
        pass

    @word_id.setter
    @abstractmethod
    def word_id(self, value: int) -> None:
        pass

    @property
    @abstractmethod
    def player_attempts(self) -> list[str]:
        pass

    @player_attempts.setter
    def player_attempts(self, value: list[str]) -> None:
        pass

    @abstractmethod
    def clear(self):
        pass
