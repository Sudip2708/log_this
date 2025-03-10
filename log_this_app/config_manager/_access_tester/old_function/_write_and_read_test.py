import os
from pathlib import Path

def _write_and_read_test(target_dir: Path):
    """
    Otestuje možnost zápisu a čtení v daném adresáři.

    Jedná se o interní pomocnou funkci pro funkci is_path_writable,
    která očekává již ověřenou cestu končící složkou.

    Args:
        target_dir (Path): Cesta k adresáři.

    Returns:
        str: Prázdný řetězec, pokud je zápis a čtení v pořádku, jinak chybová zpráva.
    """

    # Testovací soubor
    test_path = target_dir / f"_writability_test_{os.getpid()}.tmp"

    try:
        # Pokus o zápis
        with test_path.open("w") as f:
            f.write("test")

        # Pokus o čtení
        with test_path.open("r") as f:
            content = f.read()
            if not content:
                return "Zápis proběhl, ale čtení je prázdné."
            if content != "test":
                return "Zápis proběhl, ale čtení neodpovídá."

    except FileNotFoundError:
        return f"Chyba: Soubor nebyl nalezen: {test_path}"
    except PermissionError:
        return f"Chyba: Nemám dostatečná oprávnění pro zápis/čtení: {test_path}"
    except OSError as e:
        return f"Chyba: Vyskytla se chyba operačního systému: {e}"
    except Exception as e:
        return f"Neočekávaná chyba: {e}"

    finally:
        # Vždy se pokusíme odstranit testovací soubor
        if test_path.exists():
            try:
                test_path.unlink()
            except OSError as e:
                print(f"Chyba: Nepodařilo se odstranit testovací soubor: {e}")

    return ""  # Vše proběhlo v pořádku