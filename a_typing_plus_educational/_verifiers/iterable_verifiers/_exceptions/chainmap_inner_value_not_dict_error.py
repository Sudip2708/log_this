from ..._exceptions_base import VerifyParameterError


class VerifyChainMapInnerValueNotDictError(VerifyParameterError):
    """Výjimka vyvolaná při zjištění, že jedna z vnitřních map ve struktuře `ChainMap` není typu `dict`."""

    title = "\n⚠ VNITŘNÍ HODNOTA V CHAINMAP NENÍ TYPU DICT!\n"

    def __init__(self, mapping, inner_args, annotation):

        self.mapping = mapping
        self.inner_args = inner_args
        self.annotation = annotation if annotation else "(Definice anotace není známá)"

        what_happened = [
            "   - Během kontroly hodnot typu `ChainMap` byla nalezena vnitřní hodnota,\n"
            "     která není typu `dict`, což je pro validaci klíčů a hodnot nezbytné.\n",
            f"   - Typ nalezené hodnoty: {type(mapping).__name__}\n",
            f"   - Hodnota: {repr(mapping)}\n",
            f"   - Požadovaný typ: dict (nebo kompatibilní struktura)\n",
            f"   - Použitá anotace: {repr(self.annotation)}\n",
            f"   - Očekávané typy klíčů a hodnot: {self._format_items(self.inner_args)}\n",
        ]

        what_to_do = [
            "   - Ujisti se, že všechny vnitřní mapy (`.maps`) v `ChainMap` jsou typu `dict`.\n",
            "   - Pokud používáš vlastní typ, zajisti, že se chová jako `dict` a projde validací.\n",
            "   - Zkontroluj vstupní hodnotu, případně uprav datovou strukturu nebo typovou anotaci.\n"
        ]

        super().__init__(what_happened, what_to_do)
