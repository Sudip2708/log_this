#!/usr/bin/env python3

import argparse
import logging
from typing import Union
from pathlib import Path

# Předpokládám, že vaše konfigurační třída je v modulu 'config'
# Upravte import podle skutečné struktury vašeho projektu
from your_library.config import ConfigClass


def setup_logging():
    """Nastaví základní konfiguraci pro logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )


def validate_value(value: str) -> Union[int, str, bool]:
    """
    Převede string hodnotu z příkazové řádky na správný datový typ.

    Args:
        value (str): Hodnota z příkazové řádky

    Returns:
        Union[int, str, bool]: Převedená hodnota na správný datový typ
    """
    # Zkusíme převést na boolean
    if value.lower() in ('true', 'false'):
        return value.lower() == 'true'

    # Zkusíme převést na integer
    try:
        return int(value)
    except ValueError:
        pass

    # Pokud nic z výše uvedeného, vrátíme string
    return value


def main():
    """Hlavní funkce pro zpracování příkazů z příkazové řádky."""
    parser = argparse.ArgumentParser(
        description='Nástroj pro správu konfigurace vaší knihovny'
    )

    # Přidáme argumenty
    parser.add_argument(
        'key',
        help='Konfigurační klíč, který chcete změnit'
    )
    parser.add_argument(
        'value',
        help='Nová hodnota pro konfigurační klíč'
    )
    parser.add_argument(
        '--show',
        action='store_true',
        help='Zobrazí aktuální konfiguraci před a po změně'
    )

    args = parser.parse_args()

    # Nastavíme logging
    setup_logging()

    try:
        # Vytvoříme instanci konfigurační třídy
        config = ConfigClass()

        # Pokud je požadováno, zobrazíme současnou konfiguraci
        if args.show:
            logging.info("Současná konfigurace:")
            logging.info(config.config)

        # Převedeme hodnotu na správný datový typ
        value = validate_value(args.value)

        # Aktualizujeme konfiguraci
        config.update_config(args.key, value)

        # Pokud je požadováno, zobrazíme novou konfiguraci
        if args.show:
            logging.info("Nová konfigurace:")
            logging.info(config.config)

    except (KeyError, ValueError) as e:
        logging.error(f"Chyba při aktualizaci konfigurace: {str(e)}")
        exit(1)
    except Exception as e:
        logging.error(f"Neočekávaná chyba: {str(e)}")
        exit(1)


if __name__ == '__main__':
    main()