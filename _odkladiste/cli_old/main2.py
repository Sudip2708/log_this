# log_this/manager/config/cli/_main.py
from .parsers import create_parser, validate_args
from .data._setup_logging import setup_logging
from .data._handle_general_commands import handle_general_commands
from .data._handle_key_value_commands import handle_key_value_commands
from log_this.manager.config import get_config


def main() -> None:
    """Hlavní funkce pro zpracování příkazů z příkazové řádky."""
    parser = create_parser()
    args = parser.parse_args()

    setup_logging()
    config = get_config()

    try:
        # Zpracování příkazů které nepotřebují key/value
        if any([
            args.show_current,
            args.reset,
            args.export,
            args.import_file
        ]):
            handle_general_commands(args, config)
            return

        # Zpracování příkazů s klíčem a hodnotou
        handle_key_value_commands(args, config)

    except (ValueError, RuntimeError) as e:
        logging.error(f"Chyba: {str(e)}")
        exit(1)