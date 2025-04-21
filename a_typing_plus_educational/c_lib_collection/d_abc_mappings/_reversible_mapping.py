from collections.abc import ReversibleMapping

from ..._bases import BaseMappingValidator, K, V


class ReversibleMappingValidator(BaseMappingValidator):
    """
    Validátor pro zápis ReversibleMapping[K, V]

    Hint:
        ReversibleMapping = Mapping s podporou reversed()
    """

    VALIDATOR_KEY = "reversible_mapping"
    ANNOTATION = ReversibleMapping[K, V]
    INFO = "Definuje mapování s podporou reversed()"
    ORIGIN = ReversibleMapping

