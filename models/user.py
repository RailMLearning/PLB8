"""Модель User."""


class User:
    """Пользователь: уникальный идентификатор и имя."""

    def __init__(self, name: str, uid: str) -> None:
        """Инициализация пользователя.

        Args:
            name: Имя пользователя.
            uid: Уникальный идентификатор.
        """
        self.name = name
        self.id = uid

    @property
    def name(self) -> str:
        """Имя пользователя."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str) and name.strip():
            self.__name = name.strip()
        else:
            raise ValueError("Ошибка при задании имени пользователя")

    @property
    def id(self) -> str:
        """Уникальный идентификатор пользователя."""
        return self.__id

    @id.setter
    def id(self, uid: str) -> None:
        if isinstance(uid, str) and uid.strip():
            self.__id = uid.strip()
        else:
            raise ValueError("Ошибка при задании ID пользователя")
