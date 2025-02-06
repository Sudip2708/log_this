import json
from pathlib import Path
from typing import Union, Optional

from .ccc import *
from ..cli.styler import cli_print


def system_access_tester(config_path: Path):
    """
    Funkce pro otestování přístupnosti disku pro zápis, četení a mazání.

    Args:
        config_path: Cesta ke konfiguračnímu souboru
    """

    try:
        # Testy zaměřené na správnost cesty
        verify_path_instance(config_path)
        validate_path(config_path)
        validate_dir(config_path)

        # Vytvoření testovacích proměnných
        test_path = config_path.parent / "_config_test.json"
        test_data = {"test": "data"}

        # Test vytvoření souboru
        create_test_file(test_path)
        verify_test_file_creation(test_path)

        # Test čtení a zápisu souboru
        write_test_data(test_path, test_data)
        read_data = read_test_data(test_path)
        verify_test_data(read_data, test_data)

        # Test smazání souboru
        delete_test_data(test_path)
        verify_test_file_delete(test_path)

    except SystemAccessError as e:
        cli_print(
            style="warning",
            info="Inicializační kontrola zápisu a čtení z disku neprošla",
            detail="Knihovnu bude možné normálně používat. \n"
                   "Veškeré změny konfigurace je možné provést, jen nedojde k jejich uložení do konfiguračního souboru. ",
            hint=f"Zde je záznam chyby na které se ověření přístupu na disk zastavilo:\n"
                 f"- {e.message} \n"
                 f"Zde jsou doplňující informace: \n"
                 f"- {e.detail} \n"
                 f"- {e.hint}"
        )



