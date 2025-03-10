from typing import Union

from ._base_cli_exception import BaseCLIException
from ..keys import KEYS_DATA


class ValidateValueError(BaseCLIException):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    # Inicializace výjiimky
    def __init__(
            self,
            key: str,
            value: Union[int, str, bool]
    ):

        # Stručný popis výjimky
        message = f"Pro klíč '{key}' byla zadaná neplatná hodnota: '{value}'."

        # Detailnější popis výjimky (vrací tuple se stringy)
        detail = KEYS_DATA.options

        # Nápověda k dané výjimce (vrací tuple se stringy)
        hint = KEYS_DATA.hint

        # Inicializace BaseCLIException
        super().__init__(message, detail, hint)