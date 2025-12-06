"""Модель UserCurrency."""


class UserCurrency:
    """Подписка пользователя на валюту (связь многие-ко-многим)."""

    def __init__(self, id: str, user_id: str, currency_id: str) -> None:
        """Инициализация подписки.

        Args:
            id: Уникальный идентификатор подписки.
            user_id: ID пользователя.
            currency_id: ID валюты.
        """
        self.id = id
        self.user_id = user_id
        self.currency_id = currency_id

    @property
    def id(self) -> str:
        """Уникальный идентификатор подписки."""
        return self.__id

    @id.setter
    def id(self, id: str) -> None:
        if isinstance(id, str) and id.strip():
            self.__id = id.strip()
        else:
            raise ValueError("Ошибка при задании ID подписки")

    @property
    def user_id(self) -> str:
        """ID пользователя."""
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id: str) -> None:
        if isinstance(user_id, str) and user_id.strip():
            self.__user_id = user_id.strip()
        else:
            raise ValueError("Ошибка при задании user_id")

    @property
    def currency_id(self) -> str:
        """ID валюты."""
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, currency_id: str) -> None:
        if isinstance(currency_id, str) and currency_id.strip():
            self.__currency_id = currency_id.strip()
        else:
            raise ValueError("Ошибка при задании currency_id")
