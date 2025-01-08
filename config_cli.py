# log_this/manager/config/cli.py

import argparse
import logging
from typing import Union, Optional, Tuple

from .get_config import get_config


def setup_logging() -> None:
    """Nastaví základní konfiguraci pro logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )


def parse_value(value: str) -> Union[int, str, bool]:
    """
    Převede string hodnotu z příkazové řádky na správný datový typ.

    Args:
        value (str): Hodnota z příkazové řádky

    Returns:
        Union[int, str, bool]: Převedená hodnota na správný datový typ
    """
    # Převod na boolean
    if value.lower() in ('true', 'false'):
        return value.lower() == 'true'

    # Převod na integer
    try:
        return int(value)
    except ValueError:
        pass

    # Vrátíme string
    return value


def validate_args(args: argparse.Namespace) -> Tuple[bool, Optional[str]]:
    """
    Validuje argumenty z příkazové řádky.

    Args:
        args (argparse.Namespace): Argumenty z příkazové řádky

    Returns:
        Tuple[bool, Optional[str]]: (Je validní?, Chybová zpráva)
    """
    config = get_config()

    # Kontrola existence klíče
    if args.key not in config.DEFAULTS:
        return False, f"Klíč '{args.key}' není platný. Platné klíče jsou: {', '.join(config.DEFAULTS.keys())}"

    # Kontrola typu hodnoty
    try:
        value = parse_value(args.value)
        expected_type = type(config.DEFAULTS[args.key])
        if not isinstance(value, expected_type):
            return False, f"Hodnota '{args.value}' není správného typu. Očekávaný typ: {expected_type.__name__}"
    except Exception as e:
        return False, f"Chyba při zpracování hodnoty: {str(e)}"

    return True, None


def handle_config_commands(args: argparse.Namespace) -> None:
    """
    Zpracuje příkazy pro správu konfigurace.

    Args:
        args (argparse.Namespace): Argumenty z příkazové řádky
    """
    config = get_config()

    if args.show_current:
        logging.info("Aktuální konfigurace:")
        for key, value in config.config.items():
            logging.info(f"{key}: {value}")
        return

    if args.reset:
        config._reset_config()
        logging.info("Konfigurace byla resetována na výchozí hodnoty")
        return

    if args.export:
        config._export_config_to_file(args.export)
        logging.info(f"Konfigurace byla exportována do souboru: {args.export}")
        return

    if args.import_file:
        config._import_config_from_file(args.import_file)
        logging.info(
            f"Konfigurace byla importována ze souboru: {args.import_file}")
        return

    # Základní příkaz pro update konfigurace
    value = parse_value(args.value)
    original_value = config.config[args.key]

    if args.show:
        logging.info(f"Původní hodnota pro '{args.key}': {original_value}")

    config._update_config(args.key, value)

    if args.show:
        logging.info(f"Nová hodnota pro '{args.key}': {value}")


def main() -> None:
    """Hlavní funkce pro zpracování příkazů z příkazové řádky."""
    parser = argparse.ArgumentParser(
        description='Nástroj pro správu konfigurace log_this knihovny'
    )

    # Základní argumenty pro update
    parser.add_argument(
        'key',
        nargs='?',
        help='Konfigurační klíč pro změnu'
    )
    parser.add_argument(
        'value',
        nargs='?',
        help='Nová hodnota pro konfigurační klíč'
    )

    # Přepínače pro různé operace
    parser.add_argument(
        '--show',
        action='store_true',
        help='Zobrazí hodnotu před a po změně'
    )
    parser.add_argument(
        '--show-current',
        action='store_true',
        help='Zobrazí aktuální konfiguraci'
    )
    parser.add_argument(
        '--reset',
        action='store_true',
        help='Resetuje konfiguraci na výchozí hodnoty'
    )
    parser.add_argument(
        '--export',
        metavar='FILE',
        help='Exportuje konfiguraci do souboru'
    )
    parser.add_argument(
        '--import-file',
        metavar='FILE',
        help='Importuje konfiguraci ze souboru'
    )

    args = parser.parse_args()

    # Nastavení loggingu
    setup_logging()

    try:
        # Zpracování příkazů které nepotřebují key/value
        if any([args.show_current, args.reset, args.export, args.import_file]):
            handle_config_commands(args)
            return

        # Kontrola povinných argumentů pro update
        if not args.key or not args.value:
            parser.error(
                "Pro změnu konfigurace je potřeba zadat klíč a hodnotu")

        # Validace argumentů
        is_valid, error_message = validate_args(args)
        if not is_valid:
            parser.error(error_message)

        # Zpracování příkazu
        handle_config_commands(args)

    except Exception as e:
        logging.error(f"Chyba: {str(e)}")
        exit(1)


if __name__ == '__main__':
    main()