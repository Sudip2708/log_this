# log_this/manager/config/cli/_main.py
from .parsers import create_parser, validate_args
from .handlers import handle_config_commands
from .utils import setup_logging
from .data._parse_input_value import parse_input_value
from .data._handle_general_config_commands import handle_general_config_commands
from .data._handle_key_value_config_commands import handle_key_value_config_commands
from log_this_old.manager.config import get_config


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
            handle_general_config_commands(args)
            return

        # Kontrola povinných argumentů pro update
        if not args.key or not args.value:
            parser.error("Pro změnu konfigurace je potřeba zadat klíč a hodnotu")

        # Zpracování vstupní hodnoty
        value = parse_input_value(args.value)
        if not config._validate_key_and_value(args.key, value):
            parser.error("Byli zadány neplatné údaje. Žádná změna nebyla provedena.")

        # Zpracování příkazu
        handle_key_value_config_commands(args)

    except Exception as e:
        logging.error(f"Chyba: {str(e)}")
        exit(1)