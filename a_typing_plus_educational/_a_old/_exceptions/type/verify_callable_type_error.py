from ._verify_type_error import VerifyTypeError


class VerifyCallableTypeError(VerifyTypeError):
    """Výjimka vyvolaná, pokud hodnota není volatelná."""

    title = "\n⚠ ZACHYCENA NESHODA – OBJEKT NENÍ VOLATELNÝ!\n"

    def __init__(self, value):
        self._value = value

        what_happened = [
            f"   - Očekával se volatelný objekt (callable).\n",
            f"   - Předaná hodnota: {repr(value)}\n",
            f"   - Typ hodnoty: {type(value).__name__}\n"
        ]

        what_to_do = [
            "   - Ujistěte se, že předaná hodnota je funkce, metoda nebo objekt s metodou __call__.\n",
            "   - Pokud používáte lambda nebo funkci, zkontrolujte, zda jste ji správně předali.\n"
        ]

        super().__init__(what_happened, what_to_do)
