from typing import Any, Callable

from .lambda_verifier import lambda_verifier


def boolean_lambda_verifier(
    lambda_command: Callable[..., bool],
    *args: Any,
    bool_only: bool = False,
) -> bool:
    """Specializovaný validátor pro lambda příkazy vracející boolean hodnotu.

    ## Klíčové koncepty
    Tato funkce je zjednodušenou verzí lambda validátoru, zaměřenou výhradně
    na lambda příkazy, které vracejí boolean hodnotu. Slouží jako pohodlný
    wrapper kolem obecnějšího lambda validátoru.

    ## Architekturální kontext
    - Součást hierarchie validačních funkcí knihovny
    - Využívá hlavní `lambda_verifier` pro implementaci validační logiky
    - Vhodné pro validace vyžadující striktně boolean výstup

    ## Parametry
    - `lambda_command`: Lambda příkaz, který musí vracet boolean
    - `*args`: Libovolné argumenty předávané lambda příkazu
    - `bool_only`: Řídí chování při neúspěšné validaci
        - `True`: Vrací False místo vyhazování výjimky
        - `False`: Vyvolává výjimku při selhání validace

    ## Návratové hodnoty
    - `True`: Lambda příkaz proběhl úspěšně a vrátil True
    - `False`: Podle nastavení `bool_only`

    ## Výjimky
    Může vyvolat několik specializovaných výjimek:
    - `VerifyLambdaCommandNotCallableError`
    - `VerifyLambdaReturnedFalseError`
    - `VerifyLambdaParameterCountError`

    ## Příklady použití
    ```python
    # Validace objektu podle vlastní logiky
    def is_positive(x): return x > 0
    boolean_lambda_verifier(is_positive, 5)  # True
    boolean_lambda_verifier(is_positive, -1)  # Vyhodí výjimku

    # Použití s bool_only
    boolean_lambda_verifier(is_positive, -1, bool_only=True)  # False
    ```

    ## Pokročilé koncepty
    - Implementuje princip "fail fast" v validacích
    - Umožňuje flexibilní validaci lambda příkazů
    - Odděluje logiku validace od samotné validační akce
    """
    return lambda_verifier(
        lambda_command,
        *args,
        bool_only=bool_only,
        boolean_lambda_command=True
    )
