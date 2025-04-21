from ._a_base_types import _base_types
from ._b_union import _union_types
from ._c_optional import _optional_types
from ._d_list import _list_types
from ._e_tuple import _tuple_types
from ._f_dict import _dict_types
from ._g_set import _set_types
from ._h_literal import _literal_types
from ._i_callable import _callable_types
from ._j_sequence import _sequence_types
from ._k_mapping import _mapping_types


def validate_value(value, parsed_type):
    """
    Ověří hodnotu proti rozložené typové anotaci.

    Args:
        value: Hodnota k ověření
        parsed_type: Rozložená typová anotace z funkce parse_typing_annotation

    Returns:
        bool: True, pokud hodnota odpovídá typové anotaci, jinak False
    """

    # Kontrola pro základní typy (str, int, bool, atd.)
    if isinstance(parsed_type, str):
        return _base_types(value, parsed_type)

    # Kontrola pro složené typy
    if isinstance(parsed_type, dict):

        # Kontrola pro Union
        if "union" in parsed_type:
            return _union_types(value, parsed_type)

        # Kontrola pro Optional
        if "optional" in parsed_type:
            return _optional_types(value, parsed_type)

        # Kontrola pro List
        if "list" in parsed_type:
            return _list_types(value, parsed_type)

        # Kontrola pro Tuple
        if "tuple" in parsed_type:
            return _tuple_types(value, parsed_type)

        # Kontrola pro Dict
        if "dict" in parsed_type:
            return _dict_types(value, parsed_type)

        # Kontrola pro Set
        if "set" in parsed_type:
            return _set_types(value, parsed_type)

        # Kontrola pro Literal
        if "literal" in parsed_type:
            return _literal_types(value, parsed_type)

        # Kontrola pro Callable
        if "callable" in parsed_type:
            return _callable_types(value, parsed_type)

        # Kontrola pro další generické typy
        for type_name, type_args in parsed_type.items():

            if type_name == "sequence":
                return _sequence_types(value, type_name, type_args)

            if type_name == "mapping":
                return _mapping_types(value, type_name, type_args)

    # Pokud nejsme schopni rozhodnout, vrátíme False
    return False