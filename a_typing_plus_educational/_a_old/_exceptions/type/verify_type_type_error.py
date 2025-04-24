from ._verify_type_error import VerifyTypeError


class VerifyTypeTypeError(VerifyTypeError):
    """Výjimka vyvolaná při předání objektu, který není požadovanou třídou."""

    title = "\n⚠ ZACHYCENA NESHODA TYPU TŘÍDY!\n"

    def __init__(self, value, expected_classes):
        self._value = value
        self._expected_classes = expected_classes

        what_happened = [
            "   - Ověřený objekt není instancí požadované třídy typu `Type[X]`.\n",
            f"   - Předaný objekt: {repr(value)}\n",
            f"   - Typ objektu: {type(value).__name__}\n",
            f"   - Očekávaná třída/y: {self._format_expected()}\n",
            f"   - Požadavek: isinstance({self._get_name(value)}, type) a issubclass({self._get_name(value)}, {self._format_expected(raw=True)})\n"
        ]

        what_to_do = [
            "   - Předávej třídu, nikoli instanci (např. `MyClass`, ne `MyClass()`).\n",
            "   - Ujisti se, že třída dědí z požadovaného typu (např. `BaseClass`).\n"
        ]

        super().__init__(what_happened, what_to_do)

    def _format_expected(self, raw=False):
        if isinstance(self._expected_classes, tuple):
            if raw:
                return ', '.join(cls.__name__ for cls in self._expected_classes)
            return ', '.join(f"`{cls.__name__}`" for cls in self._expected_classes)
        if raw:
            return self._expected_classes.__name__
        return f"`{self._expected_classes.__name__}`"

    def _get_name(self, obj):
        if isinstance(obj, type):
            return obj.__name__
        return type(obj).__name__
