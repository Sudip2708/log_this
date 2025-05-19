from typing import Any, Callable

from ..._exceptions_base import VerifyValueError
from ._get_lambda_command import get_lambda_command


class VerifyLambdaCommandError(VerifyValueError):
    """
    Výjimka vyvolaná při chybě během vykonávání lambda příkazu.
    """

    title = "\n⚠ OVĚŘENÍ LAMBDA PŘÍKAZU VYVOLALO VÝJIMKU\n"

    def __init__(
            self,
            lambda_command: Callable[[Any], bool],
            original_exception: Exception,
            lambda_arguments: Any
    ):
        self.lambda_command = get_lambda_command(lambda_command)
        self.lambda_arguments = lambda_arguments
        self.original_exception = original_exception

        what_happened = [
            "   - Během ověření lambda příkazu došlo k vyvolání výjimky.\n",
            f"   - Lambda příkaz: {self.lambda_command}n",
            f"   - Předané parametry: {self._format_items(self.lambda_arguments)}n",
            f"   - Získané info k výjimce: {type(self.original_exception).__name__} - {str(self.original_exception)}\n"
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj, lambda příkaz a ověřte část která vyvolala výjimku.\n",
            "   - Pokud je lambda příkaz v pořádku, zkontrolujte zda není chyba v definici předaných parametrů.\n"
        ]

        super().__init__(what_happened, what_to_do, self.title)

