from pickers import config_key_picker, config_value_picker
# from log_this.manager.config import set_new_value


def run_config_settings(key: str = None) -> None:
    """Zpracuje proces změny konfigurace."""

    # Zobrazení menu pro výběr klíče
    key = key if key else config_key_picker()

    # Zobrazení dialogu pro zadání hodnoty
    value = config_value_picker(key)

    print(f"\nNastaveno: {key} = {value}")

    # Uložení do konfigurace (klíč a hodnota jsou již zvalidované)
    # set_new_value(key, value, vlaue_check=True)


