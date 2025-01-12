# log_this/manager/config/cli/handlers/_config_handler.py
import logging
import argparse

def handle_key_value_commands(args: argparse.Namespace, config) -> None:
    """
    Zpracování příkazů, které vyžadují klíč a hodnotu.

    Args:
        args (argparse.Namespace): Argumenty z příkazové řádky
        config: Konfigurace, která je validována
    """

    # Kontrola povinných argumentů pro update
    if not args.key or not args.value:
        raise ValueError(
            "Pro změnu konfigurace je potřeba zadat klíč a hodnotu"
        )

    # Zpracování vstupní hodnoty
    value = parse_input_value(args.value)
    if not config._validate_key_and_value(args.key, value):
        raise ValueError(
            "Byli zadány neplatné údaje. Žádná změna nebyla provedena."
        )

    # Kontrola zda je uveden i argument o ukázání stavu před a po
    if args.show:
        logging.info(
            f"Původní hodnota pro '{args.key}': {config[args.key]}"
        )

    # Změna hodnoty
    if config._update_config(args.key, value):
        logging.info(
            f"Úspěšná aktualizace pro '{args.key}' na hodnbotu: {value}"
        )

    # Pokud se změna hodnoty z nějakého důvodu nepodaří
    else:
        raise RuntimeError(
            f"Aktualizace pro '{args.key}' na hodnbotu: {value} se nezdařila."
        )

    # Kontrola zda je uveden i argument o ukázání stavu před a po
    if args.show:
        logging.info(
            f"Nová hodnota pro '{args.key}': {value}"
        )