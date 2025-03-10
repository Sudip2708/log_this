from ._base_cli_exception import BaseCLIException
from ..keys import allowed_keys_with_descriptions


class ValidateKeyError(BaseCLIException):
    """Vlastní výjimka pro chyby při validaci klíče pro CLI."""

    # Inicializace výjiimky
    def __init__(
            self,
            key: str
    ):

        # Stručný popis výjimky
        message = f"Byl zadán neplatný klíč: '{key}'."

        # Detailnější popis výjimky
        detail = (
            f"Klíč '{key}' není platným klíčem pro změnu konfigurace.",
        )

        # Nápověda k dané výjimce
        # Jednotlivé řádky seznamu jsou přidány dinamicky přes *
        hint = (
            "Seznam povolených klíčů:",
            *allowed_keys_with_descriptions(),
        )

        # Inicializace BaseCLIException
        super().__init__(message, detail, hint)



