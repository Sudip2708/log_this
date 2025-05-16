from typing import Any, Dict, Literal

from ..._exceptions_base import (
    VerifyUnexpectedInternalError,
    VerifyError
)
from ._exceptions import (
    VerifyDuckTypingInstructionNotDictError,
    VerifyDuckTypingInstructionEmptyError,
    VerifyDuckTypingInstructionInvalidKeyError,
    VerifyDuckTypingGetExceptionError,
    VerifyDuckTypingReturnedFalseError
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
    Validátor pro ověřování objektů podle principu duck typing.

    Na základě zadaných instrukcí ověřuje, zda objekt obsahuje požadované atributy,
    zda jsou volatelné, coroutine, celočíselné nebo splňují zadaný lambda výraz.

    Klíče instrukcí:
        - "has_attr": ověřuje přítomnost atributů.
        - "has_callable_attr": ověřuje přítomnost a volatelnost atributů.
        - "has_coroutine_attr": ověřuje, zda atributy jsou coroutine funkce.
        - "has_int_attr": ověřuje, zda atributy jsou typu `int`.
        - "lambda": spustí vlastní ověřovací výraz typu `lambda obj: bool`.

    Používá se jak interně pro typové anotace, tak externě jako validátor objektů.

    Attributes:
        VERIFIERS (Dict[str, Callable]): Mapování ověřovacích klíčů na funkce.
        VALID_KEYS (Tuple[str]): Povolené klíče pro instrukce.

    Example:
        >>> duck_typing_verifier(obj, {"has_attr": ["name", "value"]})
        True
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
        Spouští ověření objektu podle zadaných instrukcí.

        Args:
            value (Any): Objekt, který má být ověřen.
            instruction (Dict[str, Any]): Slovník s validačními pravidly.
            bool_only (bool): Pokud True, výsledek je pouze True/False.
                              Pokud False, selhání vyvolává výjimky.

        Returns:
            bool: True pokud všechny testy prošly, jinak False (pokud bool_only=True).

        Raises:
            VerifyDuckTypingInstructionNotDictError: Pokud `instruction` není slovník.
            VerifyDuckTypingInstructionEmptyError: Pokud `instruction` je prázdný.
            VerifyDuckTypingInstructionInvalidKeyError: Pokud se objeví neznámý klíč.
            VerifyDuckTypingReturnedFalseError: Pokud validace selže (a bool_only=False).
            VerifyDuckTypingGetExceptionError: Pokud některý test vyhodí ověřovací výjimku.
            VerifyUnexpectedInternalError: Pro neočekávané chyby mimo knihovnu.
        """

        # Ověření parametr instruction, zda se jedná o slovník
        if not isinstance(instruction, dict):
            raise VerifyDuckTypingInstructionNotDictError(value, instruction)

        # Ověření parametr instruction, zda obsahuje instrukce
        if not instruction:
            raise VerifyDuckTypingInstructionEmptyError(value)

        # Výsledkový slovník
        outcome = {
            "valid": [],
            "invalid": [],
            "exception": {},
        }

        try:

            # Procházení slovníku s instrukcemi pro duck typing
            for key in instruction:

                try:

                    # Načtení funkce pro ověření atributů
                    function = self.VERIFIERS.get(key, None)

                    # Pokud daný klíč neexistuje
                    if function is None:
                        raise VerifyDuckTypingInstructionInvalidKeyError(
                            value, instruction, key, self.VALID_KEYS
                        )

                    # Ověření hodnoty na základě funkce
                    if function(value, instruction[key], bool_only=True):
                        outcome["valid"].append(key)

                    # Pokud ověření je negativní
                    else:
                        outcome["invalid"].append(key)

                # Pokud je vyvolaná pro ověřžení nějaká výjimka
                except VerifyError as e:
                    outcome["exception"][key] = e

            # Pokud byla zachycena výjimka
            if outcome["exception"]:
                # Vyvolání výjimky popisující co neprošlo
                raise VerifyDuckTypingGetExceptionError(
                    value, instruction, outcome["exception"]
                )

            # Pokud nebyla vyvolaná žádná výjimka, ale některá ověření byla negativní
            if outcome["invalid"]:

                # Pokud je nastaven požadavek na boolean odpověď
                if bool_only:
                    return False

                # Vyvolání výjimky popisující co neprošlo
                raise VerifyDuckTypingReturnedFalseError(
                    value, instruction, outcome["invalid"]
                )

            # Pokud vše proběhlo v pořádku
            return True

        # Propagace všech vnitřních výjimek vyvolaných při ověřování
        except VerifyError:
            """
            VerifyDuckTypingInstructionNotDictError: Pokud `instruction` není slovník.
            VerifyDuckTypingInstructionEmptyError: Pokud `instruction` je prázdný.
            VerifyDuckTypingInstructionInvalidKeyError: Pokud se objeví neznámý klíč.
            VerifyDuckTypingReturnedFalseError: Pokud validace selže (a bool_only=False).
            VerifyDuckTypingGetExceptionError: Pokud některý test vyhodí ověřovací výjimku.
            VerifyUnexpectedInternalError: Pro neočekávané chyby mimo knihovnu.
            """
            raise

        # Zachycení všech ostatních neočekávaných výjimek
        except Exception as e:
            raise VerifyUnexpectedInternalError(e) from e


# Vytvoření výstuní funkce
duck_typing_verifier = DuckTypingVerifier()