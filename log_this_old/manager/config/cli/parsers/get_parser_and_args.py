from ._create_parser import create_parser
from ._set_values import add_set_subparser
from ._interactive_mode import add_interactive_subparser
from ._reset_to_default_values import add_reset_default_subparser
from ._reset_previous_subparser import add_reset_previous_subparser
from ._show_current_settings import add_show_current_subparser
from ._import_settings_from_file import add_import_subparser
from ._export_current_settings_to_file import add_export_subparser


def get_parser():

    # Vytvoření parseru a subparserů
    parser, subparsers = create_parser()

    # Přidání subparseru pro změnu konfigurace za pomocí klíče a hodnoty
    add_set_subparser(subparsers)

    # Přidání subparseru pro změnu konfigurace na předchozí
    add_reset_previous_subparser(subparsers)

    # Přidání subparseru pro změnu konfigurace na defaultní
    add_reset_default_subparser(subparsers)

    # Přidání subparseru pro výpis aktuálních hodnot
    add_show_current_subparser(subparsers)

    # Přidání subparseru pro expost konfigurace do souboru
    add_export_subparser(subparsers)

    # Přidání subparseru pro import konfigurace ze souboru
    add_import_subparser(subparsers)

    # Přidání subparseru pro ineraktivní režim
    add_interactive_subparser(subparsers)

    # Navrácení praseru a argumentů
    return parser