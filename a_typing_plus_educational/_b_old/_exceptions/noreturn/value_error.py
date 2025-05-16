from .._bases import VerifyTypeError


class NoReturnValueError(VerifyTypeError):
    """Výjimka pro hodnoty, které nesmí být přítomny – typ NoReturn."""

    title = "\n⚠ NEPLATNÁ HODNOTA PRO TYP `NoReturn`!\n"

    def __init__(self, value):
        self.value = value

        what_happened = [
            f"   - Byl detekován návrat hodnoty: {repr(self.value)}\n",
            f"   - Typ `NoReturn` značí, že kód nemá nikdy nic vrátit.\n"
        ]

        what_to_do = [
            "   - Zkontrolujte, zda se funkce nebo blok nemá vůbec vracet.\n",
            "   - Pokud se jedná o výjimečný stav, použijte raději výjimku než návratovou hodnotu.\n",
        ]

        super().__init__(what_happened, what_to_do)
