from typing import Optional
from log_this.manager.config.cli.styler.cli_print import cli_print

def exit_interactive_mode(message: Optional[str] = None) -> None:
    """
    Ukončí interaktivní režim s volitelnou zprávou.

    Args:
        message (Optional[str]): Zpráva zobrazená před ukončením.
    """

    if message:
        cli_print(
            "info"
            f"\n{message}"
        )

    cli_print(
        "info",
        "Ukončuji interaktivní režim..."
    )
