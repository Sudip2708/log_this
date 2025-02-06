from typing import Union

from ._base_cli_exception import BaseCLIException


class ValueIsAlreadySetError(BaseCLIException):
    """Vlastní výjimka pro chyby při validaci hodnoty pro CLI."""

    # Inicializace výjiimky
    def __init__(
            self,
            key: str,
            value: Union[int, str, bool]
    ):

        # Stručný popis výjimky
        message = f"Pro klíč '{key}' byla zadaná již nastavená hodnota: '{value}'. "

        # Detailnější popis výjimky (vrací tuple se stringy)
        detail = (
            "Konfigurační klíč již má aktuálně nastavenou hodnotu na hodnotu kterou se snažíte nastavit. ",
        )

        # Nápověda k dané výjimce (vrací tuple se stringy)
        hint = (
            "Žádná změna nebyla učiněna. ",
        )

        # Inicializace BaseCLIException
        super().__init__(message, detail, hint)