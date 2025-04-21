from typing import NoReturn

from .._base_type_validator import TypeValidator


class NoReturnValidator(TypeValidator):
    """
    Validátor pro zápis NoReturn

    Používá se např. u funkcí, které vždy vyvolávají výjimku nebo ukončují program.

    Hint:
        NoReturn = Funkce nevrací žádnou hodnotu (typicky ukončení výjimkou)

    Příklad použití:
        def exit() -> NoReturn:
    """

    VALIDATOR_KEY = "no_return"
    ANNOTATION = NoReturn
    INFO = "Definuje, že návratová hodnota funkce nesmí nastat."
    GET_ORIGIN = None

    def validate(self, value, annotation, depth_check, custom_types, bool_only):

        # NoReturn označuje, že návratová hodnota nemá existovat
        # Pokud zde ale hodnota přesto je, jde o chybu
        return self.validate_typing(value is None, bool_only=bool_only)

