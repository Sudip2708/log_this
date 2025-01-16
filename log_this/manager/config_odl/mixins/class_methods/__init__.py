from ._create_config_file import CreateConfigFileMixin
from ._delete_config_file import DeleteConfigFileMixin
from ._load_config_dict import LoadConfigDictMixin
from ._read_config_file import ReadConfigFileMixin
from ._validate_key_and_value import ValidateKeyAndValueMixin
from ._validate_config_dict import ValidateConfigDictMixin

__all__ = [
    "CreateConfigFileMixin",  # Metoda pro vytvoření konfiguračního souboru.
    "DeleteConfigFileMixin",  # Metoda pro smazání konfiguračního souboru.
    "LoadConfigDictMixin",  # Načte konfiguraci ze souboru nebo vytvoří výchozí.
    "ReadConfigFileMixin",  # eads a configuration file and returns a dictionary with configurations.
    "ValidateKeyAndValueMixin",  # Validuje konfigurační hodnotu pro daný klíč.
    "ValidateConfigDictMixin",  # Metoda pro ověření klíčů a hodnot konfiguračního slovníku.
]