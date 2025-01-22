from ._merge_with_defaults_error import MergeWithDefaultsError
from ._validate_key_error import ValidateKeyError
from ._validate_value_error import ValidateValueError
from ._confirm_delete_error import ConfirmDeleteError
from ._delete_config_file_error import DeleteConfigFileError
from ._save_config_file_error import SaveConfigFileError
from ._read_config_file_error import ReadConfigFileError
from ._validate_dict_format_error import ValidateDictFormatError

__all__ = [
    "MergeWithDefaultsError",  # Výjimka zpracovávající chyby při doplnění chybějíchích klíčů a hodnot, Eroor pro metodu '_merge_with_defaults'
    "ValidateKeyError",  # Výjimka zpracovávající chyby při validaci klíče, Eroor pro metodu '_validate_key_and_value'
    "ValidateValueError",  # Výjimka zpracovávající chyby při validaci hodnoty, Eroor pro metodu '_validate_key_and_value'
    "ConfirmDeleteError",  # Výjimka zpracovávající chyby při vytvoření konfiguračního souboru, Eroor pro metodu 'create_config_file'
    "DeleteConfigFileError",  # Eroor pro funkci 'delete_config_file' a zacycený metodou 'create_config_file'
    "SaveConfigFileError",  # Eroor pro funkci 'save_config_file' a zacycený metodou 'create_config_file'
    "ReadConfigFileError",  # Eroor pro funkci 'save_config_file' a zacycený metodou '_read_existing_config'
    "ValidateDictFormatError",  # Eroor pro funkci 'validate_dict_format' a zacycený metodou '_read_existing_config'
]