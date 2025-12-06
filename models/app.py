"""Модель App."""

from .author import Author


class App:
    """Приложение: название, версия и автор."""

    def __init__(self, name: str, version: str, author: Author) -> None:
        """Инициализация приложения.

        Args:
            name: Название приложения.
            version: Версия приложения.
            author: Объект Author.
        """
        self.name = name
        self.version = version
        self.author = author

    @property
    def name(self) -> str:
        """Название приложения."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str) and name.strip():
            self.__name = name.strip()
        else:
            raise ValueError("Ошибка при задании названия приложения")

    @property
    def version(self) -> str:
        """Версия приложения."""
        return self.__version

    @version.setter
    def version(self, version: str) -> None:
        if isinstance(version, str) and version.strip():
            self.__version = version.strip()
        else:
            raise ValueError("Ошибка при задании версии приложения")

    @property
    def author(self) -> Author:
        """Автор приложения."""
        return self.__author

    @author.setter
    def author(self, author: Author) -> None:
        if isinstance(author, Author):
            self.__author = author
        else:
            raise ValueError("Ошибка при задании автора приложения")
