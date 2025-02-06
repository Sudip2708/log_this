import json
from pathlib import Path
from dataclasses import dataclass
from typing import Union, Tuple


@dataclass
class SystemAccessStatus:
    """Třída reprezentující výsledek testu přístupu k systému."""
    is_available: bool
    message: str
    detail: str = ""
    hint: str = ""


def validate_path(path: Union[Path, str]) -> Tuple[
    bool, Path, SystemAccessStatus]:
    """Ověří validitu cesty."""
    try:
        path = Path(path).resolve(strict=False)
        return True, path, SystemAccessStatus(True, "Cesta je validní")
    except RuntimeError:
        return False, None, SystemAccessStatus(
            False,
            "Neplatná cesta",
            f"Cesta '{path}' není platnou cestou v systému",
            "Zkontrolujte, zda cesta neobsahuje nepovolené znaky"
        )


def ensure_directory(directory: Path) -> SystemAccessStatus:
    """Zajistí existenci adresáře."""
    try:
        directory.mkdir(parents=True, exist_ok=True)
        return SystemAccessStatus(True, "Adresář je dostupný")
    except PermissionError:
        return SystemAccessStatus(
            False,
            "Nelze vytvořit adresář",
            f"Nemáte oprávnění vytvořit adresář v '{directory}'",
            "Zkontrolujte oprávnění nebo zvolte jinou cestu"
        )


def create_test_file(test_file: Path) -> SystemAccessStatus:
    """Vytvoří testovací soubor."""
    try:
        test_file.touch()
        return SystemAccessStatus(True, "Soubor vytvořen")
    except PermissionError:
        return SystemAccessStatus(
            False,
            "Nelze vytvořit soubor",
            f"Nemáte oprávnění vytvořit soubor '{test_file}'",
            "Zkontrolujte oprávnění k zápisu"
        )


def write_test_data(test_file: Path) -> Tuple[bool, dict, SystemAccessStatus]:
    """Zapíše testovací data do souboru."""
    test_data = {"test": "data"}
    try:
        with test_file.open('w', encoding='utf-8') as f:
            json.dump(test_data, f)
        return True, test_data, SystemAccessStatus(True, "Data zapsána")
    except PermissionError:
        return False, None, SystemAccessStatus(
            False,
            "Nelze zapisovat do souboru",
            f"Nemáte oprávnění zapisovat do '{test_file}'",
            "Zkontrolujte oprávnění k zápisu"
        )


def verify_test_data(test_file: Path, test_data: dict) -> SystemAccessStatus:
    """Ověří přečtená data proti původním."""
    try:
        with test_file.open('r', encoding='utf-8') as f:
            read_data = json.load(f)

        if read_data == test_data:
            return SystemAccessStatus(True, "Data ověřena")
        return SystemAccessStatus(
            False,
            "Chyba integrity dat",
            "Přečtená data neodpovídají zapsaným datům",
            "Může jít o problém s diskem nebo právy"
        )
    except (PermissionError, json.JSONDecodeError):
        return SystemAccessStatus(
            False,
            "Nelze číst data",
            f"Problém při čtení souboru '{test_file}'",
            "Zkontrolujte oprávnění ke čtení"
        )


def cleanup_test_file(test_file: Path) -> SystemAccessStatus:
    """Smaže testovací soubor."""
    try:
        if test_file.exists():
            test_file.unlink()
            if not test_file.exists():
                return SystemAccessStatus(True, "Soubor smazán")
        return SystemAccessStatus(
            False,
            "Nelze smazat soubor",
            f"Soubor '{test_file}' se nepodařilo smazat",
            "Zkontrolujte oprávnění nebo zda není soubor používán"
        )
    except PermissionError:
        return SystemAccessStatus(
            False,
            "Nelze smazat soubor",
            f"Nemáte oprávnění smazat soubor '{test_file}'",
            "Zkontrolujte oprávnění k mazání"
        )


def test_system_access(config_path: Union[Path, str]) -> SystemAccessStatus:
    """
    Otestuje dostupnost systému pomocí vytvoření testovacího JSON souboru.
    """
    # Validace cesty
    success, path, status = validate_path(config_path)
    if not success:
        return status

    # Příprava testovacího souboru
    test_file = path.parent / "_config_test.json"

    # Test adresáře
    status = ensure_directory(path.parent)
    if not status.is_available:
        return status

    # Vytvoření souboru
    status = create_test_file(test_file)
    if not status.is_available:
        return status

    # Zápis dat
    success, test_data, status = write_test_data(test_file)
    if not success:
        cleanup_test_file(test_file)
        return status

    # Ověření dat
    status = verify_test_data(test_file, test_data)
    if not status.is_available:
        cleanup_test_file(test_file)
        return status

    # Úklid
    status = cleanup_test_file(test_file)
    if not status.is_available:
        return status

    return SystemAccessStatus(
        True,
        "Systém je dostupný",
        f"Úspěšně otestován přístup k adresáři '{path.parent}'",
        ""
    )