from ..pickers import config_key_picker, config_value_picker
from ..dialogs import exit_interactive_mode, show_help
from ..exceptions import ExitInteractiveMode, ValueIsAlreadySet, ValueIsNotValid


def run_config_settings() -> None:
    """Zpracuje proces změny konfigurace."""
    try:
        # Zobrazení menu pro výběr klíče
        key = config_key_picker()

        # Zobrazení dialogu pro zadání hodnoty
        value = config_value_picker(key)

        # Uložení do konfigurace (klíč a hodnota jsou již zvalidované)
        set_new_value(key, value, vlaue_check=True)

    except ExitInteractiveMode as e:
        exit_interactive_mode(e.message)

    except (ValueIsAlreadySet, ValueIsNotValid) as e:
        exit_options(e.message)

    except KeyboardInterrupt:
        exit_interactive_mode("Přerušeno uživatelem.")
