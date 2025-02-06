import json
from pathlib import Path
from typing import Union, Optional



class SystemAccessError(Exception):
    def __init__(self, message: str, detail: str = "", hint: str = ""):
        self.message = message
        self.detail = detail
        self.hint = hint
        super().__init__(self.message)


def verify_path_instance(path) -> Optional:
    """Ověří validitu cesty."""
    if isinstance(path, Path)
        return True

    else:
        raise SystemAccessError(
            message="Cesta není zapsaná jako Path instance",
            detail=f"Cesta '{path}' nemá formát platné cesty v systému.",
            hint="Pro použití cesty v rámci sitému je potřeba ji pčřevést na instanci Path."
        )


def validate_path(path) -> Optional:
    """Ověří validitu cesty."""
    try:
        path = Path(path).resolve(strict=False)
        return True

    except RuntimeError:
        raise SystemAccessError(
            message="Neplatná cesta",
            detail=f"Cesta '{path}' nemá formát platné cesty v systému.",
            hint="Zkontrolujte, zda cesta neobsahuje nepovolené znaky."
        )


def validate_dir(path) -> Optional:
    """Ověří adresář cesty."""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        return True

    except PermissionError:
        raise SystemAccessError(
            message="Nelze vytvořit adresář",
            detail=f"Nemáte oprávnění vytvořit adresář v '{path.parent}'.",
            hint="Zkontrolujte oprávnění nebo zvolte jinou cestu."
        )


def create_test_file(test_path) -> Optional:
    """Otestuje vytvoření testovacího souboru."""

    try:
        test_path.touch()
        return test_path

    except PermissionError:
        raise SystemAccessError(
            message="Nelze vytvořit soubor",
            detail=f"Nemáte oprávnění vytvořit soubor '{test_path}'.",
            hint="Zkontrolujte oprávnění k zápisu."
        )

def verify_test_file_creation(test_path):
    """Ověří zda došlo k vytvoření testovacího souboru"""

    if test_path.exist():
        return test_path

    else:
        raise SystemAccessError(
            message="Vytvoření testovacího souboru se nezdařilo.",
            detail=f"Testovací soubor není k dispozici na daném umístění '{test_path}'.",
            hint="Zkontrolujte oprávnění k zápisu. Testovací soubor měl být vytvořen, ale fizicky není přítomen."
        )

def write_test_data(test_path, test_data) -> Optional:
    """Otestuje zápis dat."""

    try:
        with test_path.open('w', encoding='utf-8') as f:
            json.dump(test_data, f)
        return test_path

    except PermissionError:
        raise SystemAccessError(
            message="Nelze zapisovat do souboru",
            detail=f"Nemáte oprávnění zapisovat do '{test_file}'.",
            hint="Zkontrolujte oprávnění k zápisu."
        )


def read_test_data(test_path) -> Optional:
    """Otestuje čtení dat."""

    try:
        with test_path.open('r', encoding='utf-8') as f:
            read_data = json.load(f)
        return read_data

    except PermissionError:
        raise SystemAccessError(
            message="Nelze číst data",
            detail=f"Problém při čtení souboru '{test_path}'.",
            hint="Zkontrolujte oprávnění ke čtení."
        )

def verify_test_data(read_data, test_data) -> bool:
    """Ověří přečtená data."""

    if read_data == test_data:
        return True

    else:
        raise SystemAccessError(
            message="Chyba integrity dat.",
            detail=f"Přečtená data neodpovídají zapsaným datům. Zapsaná data: {test_data}. Načtená data po zápisu: {read_data}.",
            hint="Může jít o problém s diskem nebo právy."
        )

def delete_test_data(test_path) -> Optional:
    """Otestuje smazání souboru."""

    try:
        test_path.unlink()
        return True

    except PermissionError:
        raise SystemAccessError(
            message="Nelze smazat soubor",
            detail=f"Nemáte oprávnění smazat soubor '{test_path}'.",
            hint="Zkontrolujte oprávnění k mazání."
        )

def verify_test_file_delete(test_path):
    """Ověří zda došlo k vytvoření testovacího souboru"""

    if not test_path.exist():
        return True

    else:
        raise SystemAccessError(
            message="Smazání testovacího souboru se nezdařilo.",
            detail=f"Testovací soubor i přes provedení smazání je stále přítomen: '{test_path}'.",
            hint="Zkontrolujte oprávnění k mazání."
        )
