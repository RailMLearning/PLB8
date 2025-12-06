"""Модель Author."""

class Author:
    """Автор приложения: хранит имя и учебную группу."""

    def __init__(self, name: str, group: str) -> None:
        """Инициализация автора.

        Args:
            name: Имя автора.
            group: Учебная группа.
        """
        self.name = name
        self.group = group

    @property
    def name(self) -> str:
        """Имя автора."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str) and name.strip():
            self.__name = name.strip()
        else:
            raise ValueError("Ошибка при задании имени автора")

    @property
    def group(self) -> str:
        """Учебная группа автора."""
        return self.__group

    @group.setter
    def group(self, group: str) -> None:
        if isinstance(group, str) and group.strip():
            self.__group = group.strip()
        else:
            raise ValueError("Ошибка при задании группы автора")
