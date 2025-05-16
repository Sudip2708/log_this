from ._value_base import VerifyValueError


class VerifyHasAttributeValueError(VerifyValueError):

    # Specifický nadpis pro chyby chybějících atributů
    title = "\n⚠ ZACHYCENA NESHODA OČEKÁVANÝCH ATRIBUTŮ!\n"

    def __init__(self, value, expected_attributes):
        """
        Inicializuje výjimku s informacemi o chybějících atributech.

        Vytváří detailní zprávu obsahující informace o ověřované hodnotě,
        očekávaných atributech a konkrétních atributech, které chybí.

        Args:
            value (Any): Hodnota (objekt), která neprošla validací atributů.
            expected_attributes (Iterable[str]): Seznam nebo jiná iterovatelná
                struktura obsahující názvy očekávaných atributů.

        Algoritmus:
        ----------
        1. Uložení reference na původní hodnotu a očekávané atributy.
        2. Volání pomocné funkce `get_missing_attributes()` pro zjištění chybějících atributů.
        3. Uložení seznamu chybějících atributů.
        4. Vytvoření informativní zprávy s detaily o chybějících atributech.
        5. Sestavení praktických pokynů k nápravě problému.
        6. Inicializace nadřazené výjimky s formátovanou zprávou.

        Poznámky:
        --------
        Zpráva výjimky obsahuje reprezentaci hodnoty pomocí `repr()`, což
        pomáhá při diagnostice, zvláště pokud má objekt složitější strukturu.
        Použití `_format_items()` zajišťuje jednotný formát výpisu seznamů.
        """
        # Uložení hodnot pro diagnostiku
        self.value = value
        self.expected_attributes = expected_attributes
        self.missing = self._get_missing_attributes()

        # Vytvoření popisu problému
        what_happened = [
            "   - Ověřovaná hodnota nemá všechny potřebné atributy.\n"
            f"   - Ověřovaná hodnota: {repr(self.value)}\n",
            f"   - Očekávané atributy: {self._format_items(self.expected_attributes)}\n",
            f"   - Chybějící atributy: {self._format_items(self.missing)}\n"
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj definici hodnoty, kterou předáváš k ověření.\n",
            "   - Ujisti se, že obsahuje všechny potřebné atributy.\n"
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)

    def _get_missing_attributes(self):
        """
        Vrací seznam atributů, které chybí v ověřované hodnotě.

        Tato metoda prochází očekávané atributy a pomocí `hasattr()` určí,
        které z nich nejsou přítomny v objektu `self.value`.

        Výkonová poznámka:
        ------------------
        Neošetřuje chyby uvnitř `hasattr()`, protože tato výjimka je volána až
        poté, co vstupní hodnota byla ověřena jiným verifikátorem. Pokud by
        vstup nebyl vhodný pro introspekci, došlo by k selhání dříve. Tato metoda
        tedy předpokládá, že vstupní data jsou validní a připravená k použití.

        Returns:
            List[str]: Seznam názvů atributů, které v objektu chybí.
        """
        return [
            attr
            for attr in self.expected_attributes
            if not hasattr(self.value, attr)
        ]