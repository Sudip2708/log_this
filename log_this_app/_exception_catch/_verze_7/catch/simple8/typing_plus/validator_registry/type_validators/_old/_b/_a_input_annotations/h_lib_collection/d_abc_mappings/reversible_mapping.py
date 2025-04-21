from collections.abc import ReversibleMapping

from ..._base_mapping_validator import BaseMappingValidator
from ..._base_type_variables import K, V


class ReversibleMappingValidator(BaseMappingValidator):
    """
    Validátor pro zápis ReversibleMapping[K, V]

    Hint:
        ReversibleMapping = Mapping s podporou reversed()
    """

    VALIDATOR_KEY = "reversible_mapping"
    ANNOTATION = ReversibleMapping[K, V]
    INFO = "Definuje mapování s podporou reversed()"
    GET_ORIGIN = ReversibleMapping

