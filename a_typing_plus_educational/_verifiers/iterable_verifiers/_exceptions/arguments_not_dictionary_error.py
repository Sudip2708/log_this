from ..._exceptions_base import VerifyParameterError


class VerifyArgumentsNotDictionaryError(VerifyParameterError):
    """Výjimka vyvolaná při zjištění, že `get_args` pro slovníkovou anotaci nevrátil dvě hodnoty."""

    title = "\n⚠ NEPLATNÝ POČET VNITŘNÍCH TYPŮ VE SLOVNÍKOVÉ ANOTACI!\n"

    def __init__(self, inner_args, annotation):

        self.inner_args = inner_args
        self.annotation = annotation if annotation else "(Definice anotace není známá)"

        what_happened = [
            "   - Při pokusu o získání vnitřních typů pro slovníkovou anotaci zjištěn neplatný počet.\n",
            "   - Pro slovníkovou anotaci jsou očekávané dva typy pro klíč a hodnotu.\n",
            f"   - Zadaná anotace: {repr(self.annotation)}"
            f"   - Počet vnitřních anotací: {len(self.inner_args)}\n",
            f"   - Výpis vnitřních anotací: {self._format_items(self.inner_args)}\n",
        ]

        what_to_do = [
            "   - Zkontroluj definici anotace kterou jste předali.\n",
            "   - Ujisti se, že odpovídá formátu slovníku se dvěma typy: jeden pro klíč, druhý pro hodnotu, např. `dict[str, int]`.\n",
            "   - Pokud hodnota kterou má definovat anotace není slovníkem, změnte definici anotace hodnoty.\n"
        ]

        super().__init__(what_happened, what_to_do)
