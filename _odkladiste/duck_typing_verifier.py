from typing import Any, Dict, Literal

from ..._exceptions_base import (
    VerifyUnexpectedInternalError,
    VerifyError
)
from ._exceptions import (
    VerifyDuckTypingInstructionNotDictError,
    VerifyDuckTypingInstructionInvalidKeyError
)
from ...attribute_verifiers import (
    has_attribute_verifier,
    has_callable_attribute_verifier,
    has_coroutine_attribute_verifier
)
from ._functions import (
    has_int_attribute_verifier,
    lambda_command_attribute_verifier
)


class DuckTypingVerifier:
    """
    "has_attr": Pokud jsou zde atributy pro ověření přítomnosti
    "has_callable_attr": Pokud jsou zde atributy pro ověření přítomnosti a volatelnosti
    "has_corountine_attr": Pokud jsou zde atributy pro ověření přítomnosti a corountine funkce (pouze pro typing.AsyncContextManager)
    "has_int_attr": Pokud jsou zde atributy pro ověření přítomnosti a že jsou typu int (pro datetime anotace)
    "lambda": Pokud je zde pro ověření zadaný lambda příkaz

    """

    # Slovník zprostředkující jednotlivé validační metody
    VERIFIERS = {
        "has_attr": has_attribute_verifier,
        "has_callable_attr": has_callable_attribute_verifier,
        "has_coroutine_attr": has_coroutine_attribute_verifier,
        "has_int_attr": has_int_attribute_verifier,
        "lambda": lambda_command_attribute_verifier
    }

    # Tuple obsahující validní klíče tohoto slovníku
    VALID_KEYS = tuple(VERIFIERS.keys())

    def __call__(
            self,
            value: Any,
            instruction: Dict[str, Any],
            bool_only: bool = False,
    ):
        """
        Metoda pro ověření objektu na základě duck typing.

        Celá třída slouží k ověření hodnot na základě podobnosti chování atributů vůči svému vzoru.
        Funkce pro ověření očekává slovník s údaji pro ověření.

        Jeli použita interně v rámci validace prostřednictvím typových anotací,
        pak již každá anotace má předpřipraven tento slovník.

        Pro použití mimo tuto knihovnu, je potřeba zkontrolovat,
        zda má metoda již definovaný způsob vyřízení, a pokud nemá, můžete daný způsob definovat sami,
        nebo můžete použít jednoduší cestu, skrze předání ověření pomoci lambda funkce.

        V takovou chvíli klíč by měl být "lambda" a její logika by měla očekávat pouze jeden vstup,
        a tím je ověřovaný objekt.
        """

        # Ověření parametr instruction, zda se jedná o slovník
        if not isinstance(instruction, dict):
            raise VerifyDuckTypingInstructionNotDictError(value, instruction)

        try:

            # Procházení slovníku s instrukcemi pro duck typing
            for key in instruction:

                # Načtení funkce pro ověření atributů
                function = self.VERIFIERS.get(key, None)

                # Pokud je funkce, ověř atributy
                if function:
                    return function(value, instruction[key], bool_only)

                # Jinak vyhoď výjimku pro nevalidní instrukce
                raise VerifyDuckTypingInstructionInvalidKeyError(
                    value, instruction, key, self.VALID_KEYS
                )

        # Propagace všech vnitřních výjimek vyvolaných při ověřování
        except VerifyError:
            raise

        # Zachycení všech ostatních neočekávaných výjimek
        except Exception as e:
            raise VerifyUnexpectedInternalError(e) from e


# Vytvoření výstuní funkce
duck_typing_verifier = DuckTypingVerifier()