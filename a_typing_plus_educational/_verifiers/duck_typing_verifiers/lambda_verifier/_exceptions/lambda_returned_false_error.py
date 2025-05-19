from typing import Any, Callable

from ..._exceptions_base import VerifyValueError
from ._get_lambda_command import get_lambda_command


class VerifyLambdaReturnedFalseError(VerifyValueError, ValueError):
    """
    Výjimka vyvolaná, pokud výsledkem lambda příkazu bylo False.
    """

    title = "\n⚠ OVĚŘOVANÝ LAMBDA PŘÍKAZ NEPROŠEL VALIDACÍ\n"

    def __init__(
            self,
            lambda_command: Callable[..., bool],
            lambda_arguments: Any,
    ):
        self.lambda_command = get_lambda_command(lambda_command)
        self.lambda_arguments = lambda_arguments

        what_happened = [
            "   - Ověření lambda příkazu vrátilo hodnotu `False`.\n",
            f"   - Lambda příkaz: {self.lambda_command}\n",
            f"   - Předané parametry: {self._format_items(self.lambda_arguments)}\n",
        ]

        what_to_do = [
            "   - Zkontroluj předané parametry, zda odpovídají očekávání lambda příkazu.\n",
            "   - Ujisti se, že je lambda příkaz správně definován a že kontroluje správnou podmínku.\n",
            "   - V případě potřeby uprav buď lambda příkaz, nebo oprav vstupní parametry.\n",
            "   - Pokud chceš místo výjimky pouze návratovou hodnotu `False`, použij parametr `bool_only=True`.\n"
        ]

        super().__init__(what_happened, what_to_do, self.title)
