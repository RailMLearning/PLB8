"""Модель Currency."""


class Currency:
    """Валюта: идентификаторы, коды, название, курс и номинал."""

    def __init__(
        self,
        id: str,
        num_code: str,
        char_code: str,
        name: str,
        value: float,
        nominal: int,
    ) -> None:
        """Инициализация валюты.

        Args:
            id: Уникальный идентификатор.
            num_code: Цифровой код.
            char_code: Символьный код.
            name: Название валюты.
            value: Курс валюты.
            nominal: Номинал.
        """
        self.id = id
        self.num_code = num_code
        self.char_code = char_code
        self.name = name
        self.value = value
        self.nominal = nominal

    @property
    def id(self) -> str:
        """Уникальный идентификатор валюты."""
        return self.__id

    @id.setter
    def id(self, id: str) -> None:
        if isinstance(id, str) and id.strip():
            self.__id = id.strip()
        else:
            raise ValueError("Ошибка при задании ID валюты")

    @property
    def num_code(self) -> str:
        """Цифровой код валюты."""
        return self.__num_code

    @num_code.setter
    def num_code(self, num_code: str) -> None:
        if isinstance(num_code, str) and num_code.strip():
            self.__num_code = num_code.strip()
        else:
            raise ValueError("Ошибка при задании цифрового кода валюты")

    @property
    def char_code(self) -> str:
        """Символьный код валюты."""
        return self.__char_code

    @char_code.setter
    def char_code(self, char_code: str) -> None:
        if isinstance(char_code, str) and char_code.strip():
            self.__char_code = char_code.strip()
        else:
            raise ValueError("Ошибка при задании символьного кода валюты")

    @property
    def name(self) -> str:
        """Название валюты."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if isinstance(name, str) and name.strip():
            self.__name = name.strip()
        else:
            raise ValueError("Ошибка при задании названия валюты")

    @property
    def value(self) -> float:
        """Курс валюты."""
        return self.__value

    @value.setter
    def value(self, value: float) -> None:
        if isinstance(value, (int, float)):
            self.__value = float(value)
        else:
            raise ValueError("Ошибка при задании курса валюты")

    @property
    def nominal(self) -> int:
        """Номинал валюты."""
        return self.__nominal

    @nominal.setter
    def nominal(self, nominal: int) -> None:
        if isinstance(nominal, (int, float)) and int(nominal) > 0:
            self.__nominal = int(nominal)
        else:
            raise ValueError("Ошибка при задании номинала валюты")
