from abc import ABC, abstractmethod
from typing import Any, Union


class ConvertValueMixin(ABC):

    @staticmethod
    def _convert_value(value: str) -> Union[int, bool, str, None]:
        """
        Převede zadanou hodnotu na správný datový typ.

        Args:
            value (str): Zadaná hodnota.

        Returns:
            Union[int, bool, str]: Převedená hodnota na odpovídající datový typ.
        """

        # Pokud je zadanou hodnotou celé číslo
        try:
            return int(value)

        # Ve všech ostatních případech
        except ValueError:

            # Kontrola zda se jedná o řetězec
            if not isinstance(value, str):
                return None

            # Převod hodnoty na malá písmena
            # a oříznutí případnýchprázdných znaků na konci a na začátku
            value_lower = value.lower().strip()

            # Kontrola zda se jedná o True
            if value_lower == 'true':
                return True

            # Kontrola zda se jedná o False
            if value_lower == 'false':
                return False

            # Pokud není zachycena, vrať hodnotu zapsanou s malími písmeny
            return value_lower

