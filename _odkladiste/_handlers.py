# log_this/manager/config/cli/data/_handlers.py


def handle_show(config):
    """Zpracuje příkaz 'show'."""
    config.show_config()


def handle_set(config, key, value):
    """Zpracuje příkaz 'set'."""
    config.set(key, value)
    print(f"Klíč '{key}' byl nastaven na hodnotu '{value}'.")


def handle_reset(config):
    """Zpracuje příkaz 'reset'."""
    config.reset()


def handle_export(config, file_path):
    """Zpracuje příkaz 'export'."""
    config.export_to_file(file_path)
    config.logger(f"Konfigurace byla exportována do souboru: {file_path}")


def handle_import(config, file_path):
    """Zpracuje příkaz 'import'."""
    config.import_to_file(file_path)
    print(f"Konfigurace byla načtena ze souboru: {file_path}")


