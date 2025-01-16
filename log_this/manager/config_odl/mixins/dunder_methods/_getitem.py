from typing import Union


class GetItemMixin:

    def __getitem__(
            self,
            key: Union[str, bool, None]
    ) -> Union[int, str, bool, None]:
        """
        Vrací hodnotu pro daný klíč, podporuje také True, False a None.

        Metoda nejprve překontroluje zda jako klíčem není True, False, nebo None.
        V takovém případě je převede na jejich textovou reprezentaci.
        Následně metoda vrátí hodnotu pro daný klíč a nebo None.

        Args:
            key (Union[str, bool, None]): Klíč, pro který se hledá hodnota.

        Returns:
            Union[int, str, bool, None]: Hodnota odpovídající klíči.
        """

        if key in (True, False, None):
            key = str(key).lower()

        return self.config.get(key, None)
