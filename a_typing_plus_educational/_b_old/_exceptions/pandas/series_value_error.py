from .._bases import VerifyTypeError


class SeriesValueError(VerifyTypeError):
    """Výjimka vyvolaná při neodpovídajícím typu pro pandas.Series."""

    title = "\n⚠ ZACHYCENA NESHODA TYPU PRO PANDAS.SERIES!\n"

    def __init__(self, value):
        self.value = value

        what_happened = [
            f"   - Ověřovaná hodnota neodpovídá požadovanému typu pandas.Series.\n",
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Typ hodnoty: {type(self.value).__name__}\n",
        ]

        what_to_do = [
            "   - Zkontroluj, zda hodnota je typu pandas.Series.\n",
            "   - Pokud je hodnota typu pandas.DataFrame, zkontroluj sloupce a řádky.\n",
        ]

        super().__init__(what_happened, what_to_do)
