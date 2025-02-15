from .get_response import GetResponseMixin
from .input_custom_int_value import InputCustomIntValueMixin


__all__ = [

    "GetResponseMixin",  # get_response()
    # Vrací výstupní reakci na daný požadavek
    # Používá atributy: 'response', 'selected_key', 'selected_value'
    # Používá metody: display_menu(), run_menu(), input_custom_int_value()

    "InputCustomIntValueMixin",  # input_custom_int_value()
    # Vrací data (nadpis a položky) pro menu pro výběr hodnoty pro daný klíč.
    # Používá atributy: 'response', 'selected_key', 'selected_value'
    # Používá metody: display_menu(), run_menu()
]