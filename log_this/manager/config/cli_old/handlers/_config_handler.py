# log_this/manager/config/cli/handlers/_config_handler.py
import logging
import argparse
from ...get_config import get_config
from ._value_handler import parse_value


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