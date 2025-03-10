from pathlib import Path
import os


class PathNotWritableError(Exception):
    """Výjimka vyvolaná, když cesta není zapisovatelná."""
    pass


def is_path_writable(path: Path) -> bool:
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
        raise TypeError(
            f"Očekáván typ {Path.__name__}, ale získán {type(path).__name__}")

    # Načtení adresy ke složce kam se má zapisovat
    target_dir = path if path.is_dir() else path.parent

    # Ověření existence složky
    if not target_dir.exists():
        try:
            target_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise PathNotWritableError(
                f"Nepodařilo se vytvořit složku: {str(e)}")

    # Ověření zda je cíl cesty složka
    if not target_dir.is_dir():
        raise PathNotWritableError("Cílová cesta není složka.")

    # Testovací soubor
    test_path = target_dir / f"_writability_test_{os.getpid()}.tmp"

    try:
        # Pokus o zápis
        with test_path.open("w") as f:
            f.write("test")

        # Pokus o čtení
        with test_path.open("r") as f:
            if f.read() != "test":
                raise PathNotWritableError(
                    "Zápis proběhl, ale čtení neodpovídá.")

        return True
    except Exception as e:
        if not isinstance(e, PathNotWritableError):
            raise PathNotWritableError(f"Neočekávaná chyba: {e}")
        raise
    finally:
        # Vždy se pokusíme odstranit testovací soubor
        if test_path.exists():
            try:
                test_path.unlink()
            except:
                pass  # Ignorujeme chyby při mazání testovacího souboru