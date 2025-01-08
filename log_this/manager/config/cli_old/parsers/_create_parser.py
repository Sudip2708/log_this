# log_this/manager/config/cli/parsers/_create_parser.py
import argparse


def create_parser() -> argparse.ArgumentParser:
    """Vytvoří a nakonfiguruje parser argumentů."""
    parser = argparse.ArgumentParser(
        description='Nástroj pro správu konfigurace log_this knihovny'
    )

    # Základní argumenty pro update
    parser.add_argument(
        'key',
        nargs='?',
        help='Název konfiguračního klíče, jehož hodnota má být změněa.'
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
        help='Zobrazí aktuální konfiguraci'
    )
    # parser.add_argument(
    #     '--show-current',
    #     action='store_true',
    #     help='Zobrazí aktuální konfiguraci'
    # )
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

    return parser