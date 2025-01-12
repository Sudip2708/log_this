# log_this/manager/config/cli/parsers/_validate_args.py
from typing import Tuple, Optional
import argparse
from ..handlers import parse_value

from log_this.manager.config import get_config


def validate_args(args: argparse.Namespace) -> Tuple[bool, Optional[str]]:
    """
    Validuje argumenty z příkazové řádky pomocí validační logiky konfigurace.

    Args:
        args (argparse.Namespace): Argumenty z příkazové řádky

    Returns:
        Tuple[bool, Optional[str]]: (Je validní?, Chybová zpráva)
    """

    # Načtení singleton konfigurační instance
    config = get_config()

    try:
        # Získání hodnoty
        value = parse_value(args.value)

        # Validace hodnoty
        if config._validate_key_and_value(args.key, value):
            return True, None

        # Pokud validace neprojde
        return False, "Validace selhala (detaily viz log výše)"

    # Pokud se v bloku try vyvolá výjimka
    except Exception as e:
        return False, f"Chyba při validaci: {str(e)}"