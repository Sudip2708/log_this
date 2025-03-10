from typing import Tuple

from ._base_cli_exception import BaseCLIException


class DeleteConfigFileError(BaseCLIException):
    """Vlastní výjimka pro chyby při mazání konfiguračního souboru."""

    # Inicializace výjiimky
    def __init__(
            self,
            message: str,
            detail: Tuple[str, ...],
            hint: Tuple[str, ...]
    ):

        # Inicializace BaseCLIException
        super().__init__(message, detail, hint)