import logging
import argparse


def handle_general_commands(args: argparse.Namespace, config) -> None:
    """
    Zpracování všeobecných příkazů pro správu konfigurace.
    
    Funkce spracovává příkazy pro ketré není potřeba klíče a hodnoty.

    Args:
        args (argparse.Namespace): Argumenty z příkazové řádky
        config: Konfigurace, která je validována
    """

    if args.show_current:
        logging.info("Aktuální konfigurace:")
        for key, value in config.items():
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