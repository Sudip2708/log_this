# log_this/manager/config/cli/_main.py
from log_this.manager.config import config, cli_log
from log_this.manager.config.cli.parsers import create_parser
from log_this.manager.config.errors import ValidateKeyError, ValidateValueError
from log_this.manager.config.cli.interactive_mode import ConfigSelectorApp


def main() -> None:
    """Hlavní funkce pro zpracování příkazů z příkazové řádky."""

    # Vytvoření parseru
    parser = create_parser(config)

    # Načtení argumentů
    args = parser.parse_args()

    try:
        # Zpracování příkazu `set`
        if args.command == "set":
            try:
                # Validace klíče a hodnoty
                config.validate_key(args.key)
                config.validate_value(args.key, args.value)

                # Nastavení nové hodnoty
                config.set_new_value(args.key, args.value, value_check=True)

            except (ValidateKeyError, ValidateValueError) as e:
                # Výstraha o chybě a spuštění interaktivního režimu
                cli_log.warning(str(e))
                cli_log.info("Spouštím interaktivní režim...")

                # Spuštění nového interaktivního režimu
                options = {
                    key: config.get_possible_values(key) for key in config.get_keys()
                }
                app = ConfigSelectorApp(options)
                app.run()

        else:
            # Pokud není rozpoznán příkaz, zobraz nápovědu
            parser.print_help()

    except (ValueError, RuntimeError) as e:
        # Vypiš výjimku a ukonči zpracování příkazu
        cli_log.error(str(e))
        exit(1)
