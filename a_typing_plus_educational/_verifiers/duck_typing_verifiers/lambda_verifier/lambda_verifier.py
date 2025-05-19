from typing import Any, Callable

from ._exceptions import (
    VerifyLambdaReturnedFalseError,
    VerifyLambdaNotReturnBooleanError,
    VerifyLambdaCommandNotCallableError,
    VerifyLambdaParameterCountError,
    VerifyLambdaCommandError
)
from ...value_verifiers import is_callable_verifier

"""Univerzální validátor lambda příkazů s pokročilou logikou ověřování.

## Klíčové koncepty
Robustní validační funkce pro lambda příkazy, která poskytuje:
- Flexibilní validaci lambda příkazů
- Podporu pro lambda příkazy s různými návratovými typy
- Detailní diagnostiku selhání validace

## Architekturální kontext
- Centrální validační funkce pro lambda příkazy
- Umožňuje flexibilní validaci bez omezení na boolean výstup
- Klíčový prvek systému validace v knihovně

## Parametry
- `lambda_command`: Lambda příkaz k validaci (libovolný typ)
- `*args`: Argumenty předávané lambda příkazu
- `bool_only`: Řídí chování při validaci
    - `True`: Vrací boolean bez vyhazování výjimek
    - `False`: Vyvolává výjimky při selhání
- `boolean_lambda_command`: Řídí striktnost validace
    - `True`: Vyžaduje boolean výstup
    - `False`: Povoluje libovolné typy výstupu

## Návratové hodnoty
- `True`: Úspěšná validace lambda příkazu
- `False`: Neúspěšná validace (podle nastavení parametrů)

## Výjimky
Pokrývá širokou škálu validačních výjimek:
- `VerifyLambdaCommandNotCallableError`
- `VerifyLambdaReturnedFalseError`
- `VerifyLambdaNotReturnBooleanError`
- `VerifyLambdaParameterCountError`
- `VerifyLambdaCommandError`

## Příklady použití
```python
# Validace s libovolným výstupem
def complex_check(x, y):
    return x > 0 and len(y) > 3

lambda_verifier(complex_check, 5, "test")  # True

# Striktní boolean validace
lambda_verifier(complex_check, 5, "test",
                boolean_lambda_command=True)  # Vyvolá výjimku, pokud nevrací bool
```

## Pokročilé koncepty
- Implementuje multi-parametrovou validaci
- Poskytuje jemnou kontrolu nad validačním procesem
- Slouží jako abstrakce nad standardními validačními mechanismy Pythonu

## Poznámky k rozšíření
- Velmi flexibilní pro tvorbu vlastních validačních strategií
- Umožňuje snadné přidávání dalších validačních logik
"""
def lambda_verifier(
    lambda_command: Callable[..., Any],
    *args: Any,
    bool_only: bool = False,
    boolean_lambda_command: bool = False
) -> bool:
    """
    Univerzální validátor lambda příkazů s pokročilou logikou ověřování.

    Výjimky které může vyvolat is_instance_verifier funkce:
        VerifyLambdaReturnedFalseError: Pokud validace selže (a bool_only=False). (VerifyValueError, ValueError)
        VerifyLambdaCommandNotCallableError: Pokud se nejedná o volatelný příkaz. (VerifyParameterError, TypeError)
        VerifyLambdaNotReturnBooleanError: Pokud byl očekávaný bool výstup, ale vrátilo se něco jiného. (VerifyParameterError)
        VerifyLambdaParameterCountError: Pokud byl zadán špatný počet parametrů nebo špatné typy. (VerifyParameterError, TypeError)
        VerifyLambdaCommandRaisedExceptionError: Pokud nastane během ověřování ne-boolen příkazu k výjimce a není požadavek na bool_only odpověď.
        VerifyLambdaCommandError: Pokud nastane během ověřování boolen příkazu k výjimce.
    """

    # Ověření zda se jedná o volatelný příkaz
    if not is_callable_verifier(lambda_command, bool_only=True):
        raise VerifyLambdaCommandNotCallableError(lambda_command)

    try:

        # Ověření podminky/podmínek příkazu
        result = lambda_command(*args)

        # Pokud je výstup boolean hodnota
        if isinstance(result, bool):
            if result:
                return True

            # Pokud je režim pouze bool, vrať False bez vyhazování výjimky
            if bool_only:
                return False

            # Jinak vyhoď výjimku pro nevalidní vyhodnocení
            raise VerifyLambdaReturnedFalseError(lambda_command, args)

        # Kontrola zda se ověřuje jen to, že je vrácen nějaký výsledek
        # (příkaz nevrací boolean hodnotu a tak pokud nevyvolá výjimku, je vždy True)
        if not boolean_lambda_command:
            return True

        # Pokud byl požadavek na ověření pouze boolean příkazu, ale vrátila se nějaká hodnota
        raise VerifyLambdaNotReturnBooleanError(lambda_command, result, args)

    # Propagace vnitřních výjimek
    except (VerifyLambdaReturnedFalseError, VerifyLambdaNotReturnBooleanError):
        raise

    # Výjimka pro špatný počet parametrů nebo špatné typy
    except TypeError as e:
        raise VerifyLambdaParameterCountError(lambda_command, args) from e

    # Výjimka, zachytávající výjimky vyvolané lambda příkazem
    except Exception as e:

        # Kontrola zda se ověřuje jen to, že je vrácen nějaký výsledek
        # (příkaz nevrací boolean hodnotu a tak pokudvyvolá výjimku, je vždy False)
        if not boolean_lambda_command:

            # Pokud je požadavek na bool only odpověď
            if bool_only:
                return False

            # Jinak vyvolej výjimku
            raise VerifyLambdaCommandRaisedExceptionError

        # Ve všech ostatních případech (pro boolean_lambda_command=True)
        raise VerifyLambdaCommandError(lambda_command, e, args) from e
