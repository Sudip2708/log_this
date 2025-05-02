from typing import SupportsBytes

from ...._bases import BaseIsInstanceValidator


class SupportsBytesValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci SupportsBytes

    """

    VALIDATOR_KEY = "supportsbytes"
    ANNOTATION = SupportsBytes

    IS_INSTANCE = SupportsBytes
    HAS_ATTRS = "__bytes__"
    CALLABLE_ATTRS = None

    DESCRIPTION = "Objekt podporující konverzi na bytes"
    LONG_DESCRIPTION = (
            "Validuje, že objekt splňuje protokol SupportsBytes, "
            "tedy implementuje metodu __bytes__, která umožňuje konverzi objektu "
            "na bytovou reprezentaci pomocí funkce bytes()."
        )

