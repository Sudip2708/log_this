import os
from pathlib import Path


def check_config_file_permissions(config_path: Path) -> bool:
    """
    Ověří, zda existuje konfigurační soubor nebo zda je možné jej vytvořit a zda je čitelný a zapisovatelný.

    Vrací:
        True  - pokud je vše v pořádku,
        False - pokud s konfiguračním souborem není možné pracovat.
    """
    try:
        # Pokud soubor existuje, zkontrolujeme práva
        if config_path.exists():
            # Zkusíme soubor otevřít pro čtení
            with config_path.open('r'):
                pass
            # Zkusíme otevřít soubor pro zápis (bez modifikace)
            with config_path.open('a'):
                pass
        else:
            # Soubor neexistuje – ověříme, že adresář, kde se má soubor vytvořit, existuje a je zapisovatelný.
            parent = config_path.parent
            if not parent.exists():
                return False  # Nebo případně se pokusit vytvořit adresář
            # Testovací zápis do dočasného souboru (nebo jen ověření přístupových práv adresáře)
            test_path = parent / ".write_test"
            with test_path.open('w') as f:
                f.write("test")
            os.remove(test_path)
        return True
    except Exception as e:
        # Log nebo debug zpráva zde může být vhodná
        return False
