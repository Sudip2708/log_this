# log_this/manager/config/cli/_main.py
import traceback

from .parsers import get_parser
from .styler import cli_print
from .interactive import (
    run_interactive_menu,
    run_interactive_teaser
)
from log_this_old.manager.config import (
    set_new_value,
    reset_previous,
    reset_default,
    import_config_from_file,
    export_config_to_file,
    print_current_settings,
)

def main() -> None:
    """Hlavní funkce pro zpracování příkazů z příkazové řádky."""

    # Načtení parseru
    parser = get_parser()

    # Načtení argumentů
    args = parser.parse_args()

    try:

        # Pokud není zadán žádný příkaz -> zobraz úvodní menu
        if args.command is None:
            run_interactive_teaser()

        # Spuštění interaktivního režimu
        elif args.command == "interactive":
            run_interactive_menu()

        # Změna konfigurace za pomoci klíče a hodnoty
        elif args.command == "set":
            set_new_value(args.key, args.value)

        # Změna konfigurace na předchozí nastavení (je-li)
        elif args.command == "reset-previous":
            reset_previous()

        # Změna konfigurace na defaultní hodnoty
        elif args.command == "reset-default":
            reset_default()

        # Zobrazení aktuální konfigurace
        elif args.command == "show-current":
            print_current_settings()

        # Uložení aktuální konfigurace do souboru
        elif args.command == "export":
            export_config_to_file(args.file)

        # Načtení konfigurace ze souboru
        elif args.command == "import":
            import_config_from_file(args.file)


        # Pokud není zadán, nebo rozpoznán příkaz
        else:
            # Zobraz nápovědu
            parser.print_help()

    # Chycení jakékoliv neznámé výjimky
    # Vloží celý traceback jako detail
    # Ukončí zadávání přes cli
    except Exception as e:
        cli_print(
            style="warning",
            info=f"Došlo k chybě! - {str(e)}",
            detail=traceback.format_exc(),
            hint=(
                "Zkuste zkontrolovat vstupní hodnoty.",
                "Podrobnosti jsou výše."
            ),
            conclusion="Pokud problém přetrvává, kontaktujte podporu."
        )
        exit(1)
