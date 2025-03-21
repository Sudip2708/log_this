# log_this/manager/config/cli/_main.py
from log_this_old.manager.config import config
from log_this_old.manager.config.cli.parsers import create_parser


def main() -> None:
    """Hlavní funkce pro zpracování příkazů z příkazové řádky."""

    # Vytvoření parseru
    parser = create_parser(config)

    # Načtení argumentů
    args = parser.parse_args()

    try:
        # Volání odpovídající funkce na základě zvoleného subparseru
        if args.command == "show":
            config.show_config()
        elif args.command == "set":
            config.set_new_value(args.key, args.value)
        elif args.command == "reset":
            config.reset_to_default()
        elif args.command == "export":
            config.export_config_to_file(args.file_path)
        elif args.command == "import":
            config.import_config_from_file(args.file_path)
        else:
            # Pokud není rozpoznán příkaz, zobraz nápovědu
            parser.print_help()

    # Pokud je během zpracování vyvolaná výjimka
    except (ValueError, RuntimeError) as e:

        # Vypiš výjimku ukonči zpracování požadavku
        config.cli_log.error(str(e))
        exit(1)
