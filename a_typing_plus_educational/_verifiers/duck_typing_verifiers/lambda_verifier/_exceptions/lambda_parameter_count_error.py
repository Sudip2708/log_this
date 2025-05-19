from typing import Any, Callable

from ...._exceptions_base import VerifyParameterError
from ._get_lambda_command import get_lambda_command


class VerifyLambdaParameterCountError(VerifyParameterError, TypeError):
    """
    Výjimka vyvolaná, pokud lambda příkaz nemůže být vykonán kvůli špatnému počtu nebo typu parametrů.
    """

    title = "\n⚠ OVĚŘOVANÝ LAMBDA PŘÍKAZ NEOBDRŽEL OČEKÁVANÉ PARAMETRY\n"

    def __init__(
            self,
            lambda_command: Callable[..., bool],
            lambda_arguments: Any,
    ):
        self.lambda_command = get_lambda_command(lambda_command)
        self.lambda_arguments = lambda_arguments

        what_happened = [
            "   - Lambda příkaz nemohl být spuštěn, protože neobdržel správný počet nebo typ parametrů.\n",
            f"   - Lambda příkaz: {self.lambda_command}\n",
            f"   - Předané parametry: {self._format_items(self.lambda_arguments)}\n",
        ]

        what_to_do = [
            "   - Zkontroluj počet a typ parametrů předávaných lambda příkazu.\n",
            "   - Ujisti se, že lambda příkaz akceptuje právě tolik parametrů, kolik předáváš.\n",
            "   - V případě potřeby uprav lambda příkaz nebo volání.\n"
        ]

        super().__init__(what_happened, what_to_do, self.title)
