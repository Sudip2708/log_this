from ..pickers import config_key_picker, config_value_picker
from ..dialogs import exit_interactive_mode
from ..exceptions import ExitInteractiveMode, ValueIsAlreadySet, ValueIsNotValid
from .run_config_exit_options import run_config_exit_options
from log_this_old.manager.config import set_new_value


def run_config_settings(key: str = None) -> None:
    """Zpracuje proces změny konfigurace."""

    try:
        # Zobrazení menu pro výběr klíče
        key = key if key else config_key_picker()

        # Zobrazení dialogu pro zadání hodnoty
        value = config_value_picker(key)

        # Uložení do konfigurace (klíč a hodnota jsou již zvalidované)
        set_new_value(key, value, vlaue_check=True)

    # Zpracování špatného zadání klíče a hodnoty
    except (ValueIsAlreadySet, ValueIsNotValid) as e:
        run_config_exit_options(e.message)

    # Zpracování požadavku pro ukončení interaktivního režimu
    except ExitInteractiveMode as e:
        exit_interactive_mode(e.message)

    # Zpracování přeručení interaktivního režimu klávesovou zkratkou
    except KeyboardInterrupt:
        exit_interactive_mode("Přerušeno uživatelem.")
