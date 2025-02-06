from typing import Union, Tuple
from ..cli.styler import cli_print

def print_exceptions_warning(
        exception: BaseException,
        conclusion: Union[Tuple[str, ...], str] = ""
):
    """Funkce pro CLI výpis chyby."""

    if not isinstance(exception, BaseException):
        raise TypeError(f"Expected an exception of type BaseException, got {type(exception).__name__}.")

    detail = getattr(exception, 'detail', "")
    hint = getattr(exception, 'hint', "")

    cli_print(
        style="warning",
        info=str(exception),
        detail=detail,
        hint=hint,
        conclusion=conclusion
    )
