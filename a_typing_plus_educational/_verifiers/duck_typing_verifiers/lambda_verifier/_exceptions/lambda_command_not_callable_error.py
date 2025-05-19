from typing import Any, Callable

from ..._exceptions_base import VerifyParameterError
from ._get_lambda_command import get_lambda_command


class VerifyLambdaCommandNotCallableError(VerifyParameterError, TypeError):

    # Specifický nadpis pro chyby nesprávného typu parametru
    title = "\n⚠ OVĚŘOVANÝ LAMBDA PŘÍKAZ NENÍ VOLATELNÝ!\n"

    def __init__(
            self,
            lambda_command: Callable[[Any], bool],
    ):

        # Uložení hodnoty pro diagnostiku
        self.lambda_command = get_lambda_command(lambda_command)

        # Vytvoření popisu problému
        what_happened = [
            "   - Funkci pro ověření objektu na základě lambda příkazu byl zadán nevalidní lambda příkaz.\n",
            "   - Lambda příkaz neprošel ověřením, zda je volatelný.\n",
            f"   - Lambda příkaz: {self.lambda_command}.\n",
        ]

        # Vytvoření pokynů k nápravě
        what_to_do = [
            "   - Zkontroluj definici příkazu a oprav jej tak, aby byl volatelný.\n",
            "   - Ujisti se, že jsi předal skutečný výraz (např. `lambda x: ...`), ne výsledek jeho volání.\n",
            "   - - Například místo `lambda_command=obj.check()` použij `lambda_command=lambda obj: obj.check()`.\n",
        ]

        # Inicializace nadřazené výjimky
        super().__init__(what_happened, what_to_do, self.title)