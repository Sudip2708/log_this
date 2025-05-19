from typing import Any, Callable

from ..._exceptions_base import VerifyParameterError
from ._get_lambda_command import get_lambda_command


class VerifyLambdaNotReturnBooleanError(VerifyParameterError):
    """
    Výjimka vyvolaná, pokud výsledkem lambda příkazu nebyla boolean hodnota.
    """

    title = "\n⚠ OVĚŘOVANÝ LAMBDA PŘÍKAZ NEVRACÍ BOOLEAN HODNOTU\n"

    def __init__(
            self,
            lambda_command: Callable[..., bool],
            result: Any,
            lambda_arguments: Any,
    ):
        self.lambda_command = get_lambda_command(lambda_command)
        self.result = result
        self.lambda_arguments = lambda_arguments

        what_happened = [
            "   - Ověření lambda příkazu nevrátilo boolean hodnotu.\n",
            f"   - Lambda příkaz: {self.lambda_command}\n",
            f"   - Předané parametry: {self._format_items(self.lambda_arguments)}\n",
            f"   - Navrácená hodnota: {self.result}\n",
        ]

        what_to_do = [
            "   - Zkontroluj předané parametry, zda odpovídají očekávání lambda příkazu.\n",
            "   - Ujisti se, že je lambda příkaz správně definován a že kontroluje správnou podmínku.\n",
            "   - V případě potřeby uprav buď lambda příkaz, nebo oprav vstupní parametry.\n",
            "   - Pokud chceš místo výjimky pouze návratovou hodnotu `False`, použij parametr `bool_only=True`.\n"
        ]

        super().__init__(what_happened, what_to_do, self.title)
