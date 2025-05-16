from .._bases import VerifyTypeError


class DataFrameValueError(VerifyTypeError):
    """Výjimka vyvolaná při neodpovídajícím typu pro pandas.DataFrame."""

    title = "\n⚠ ZACHYCENA NESHODA TYPU PRO PANDAS.DATAFRAME!\n"

    def __init__(self, value):
        self.value = value

        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá požadovanému typu pandas.DataFrame.\n",
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
        ]

        what_to_do = [
            "   - Zkontroluj, zda hodnota je typu pandas.DataFrame.\n",
            "   - Pokud je hodnota typu pandas.Series, ověř její sloupce a řádky.\n",
        ]

        super().__init__(what_happened, what_to_do)
