from pathlib import Path
import os

from ._write_and_read_test import _write_and_read_test


def is_path_writable(path: Path):
    """
    Ověří, zda je možné zapisovat na danou cestu.

    Args:
        path (Path): Cesta ke složce nebo souboru.

    Returns:
        bool: True, pokud je zápis možný.

    Raises:
        TypeError: Pokud path není instancí Path.
        PathNotWritableError: Pokud nelze zapisovat s popisem konkrétního problému.
    """

    # Ověření, zda path je instancí Path
    if not isinstance(path, Path):
        return (f"Cesta není zadaná jako instance Path! "
                f"Očekáván typ: {Path.__name__}, "
                f"získáný typ: {type(path).__name__}")

    # Načtení adresy ke složce kam se má zapisovat
    target_dir = (path if path.is_dir() else path.parent)

    # Ověření zda je cílová složka cesty je složka
    if not target_dir.is_dir():
        return "Cílová cesta není složka."

    # Ověření existence složky
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        return f"Chyba: Některá z rodičovských složek je soubor: {target_dir}"
    except FileNotFoundError:
        return f"Chyba: Nemám dostatečná oprávnění k vytvoření adresáře: {target_dir}"
    except PermissionError:
        return f"Chyba: Nemám dostatečná oprávnění k vytvoření adresáře: {target_dir}"
    except OSError as e:
        return f"Chyba: Vyskytla se chyba operačního systému: {e}"
    except Exception as e:
        return f"Neočekávaná chyba: {e}"

    # Testování možnosti zápisu a čtení
    return _write_and_read_test(target_dir)


