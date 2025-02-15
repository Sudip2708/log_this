from typing import List, Dict, Union
from .keys_data_dict import KEYS_DATA

def validate_config_dictionary(
        config_dict: Dict[str, Union[int, str, bool]]
) -> bool:
    """Funkce pro rychlé ověření validačních dat pro metodu restore_last_snapshot()"""

    # Kontrola zda se jedná o instanci slovníku
    if not isinstance(config_dict, dict):
        print(f"Config dict není instance slovníku. Zjištěná instance: {type(config_dict)}")
        return False

    # Kontrola zda se shodují klíče
    if set(config_dict.keys()) != set(KEYS_DATA.keys()):
        print(f"Config dict nemá shodný obsah klíčů.")
        return False

    # Validace hodnoty
    for key, value in config_dict.items():
        if not KEYS_DATA[key].validate(value):
            print(f"Klíč {key} nemá uvedenu validní hodnotu: {value}.")
            return False

    # Pokud všechny kontroly proběhnou v pořádku
    return True
