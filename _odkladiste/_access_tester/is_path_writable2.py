from pathlib import Path

def is_path_writable(path: Path) -> tuple[bool, str | None]:
    """
    Ověří, zda je možné zapisovat na danou cestu.

    Args:
        path (Path): Cesta ke složce nebo souboru.

    Returns:
        Tuple[bool, str | None]: True, pokud je zápis možný, jinak False a chybová zpráva.
    """

    # Ověření, zda path je instancí Path
    if not isinstance(path, Path):
        raise TypeError(
            f"Očekáván typ {Path.__name__}, ale získán {type(path).__name__}")

    try:

        # Načtení adresy ke složkce kam se má zapisovat
        target_dir = path if path.is_dir() else path.parent

        # Ověření existence složky
        if not target_dir.exists():
            try:
                target_dir.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                return False, f"Nepodařilo se vytvořit složku: {str(e)}"

        # Ověření zda je cíl cesty složka
        if not target_dir.is_dir():
            return False, "Cílová cesta není složka."

        # Testovací soubor
        test_path = target_dir / "_writability_test.tmp"

        # Pokus o zápis
        with test_path.open("w") as f:
            f.write("test")

        # Pokus o čtení
        with test_path.open("r") as f:
            if f.read() != "test":
                return False, "Zápis proběhl, ale čtení neodpovídá."

        # Pokus o smazání
        test_path.unlink()

        return True, None

    except Exception as e:
        return False, f"Neočekávaná chyba: {e}"
