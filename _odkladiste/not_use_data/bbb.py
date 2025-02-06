import json
from pathlib import Path
from dataclasses import dataclass
from typing import Union, Optional


@dataclass
class SystemAccessStatus:
    """Třída reprezentující výsledek testu přístupu k systému."""
    is_available: bool
    message: str
    detail: str = ""
    hint: str = ""


class SystemAccessTester:
    """Třída pro testování dostupnosti systému pro konfigurační soubory."""

    def __init__(self, config_path: Union[Path, str]):
        """
        Inicializuje tester s cestou ke konfiguračnímu souboru.

        Args:
            config_path: Cesta ke konfiguračnímu souboru
        """
        self.original_path = config_path
        self.path: Optional[Path] = None
        self.test_file: Optional[Path] = None
        self.test_data: dict = {"test": "data"}
        self.status: Optional[SystemAccessStatus] = None

    def validate_path(self) -> bool:
        """Ověří validitu cesty."""
        try:
            self.path = Path(self.original_path).resolve(strict=False)
            return True
        except RuntimeError:
            self.status = SystemAccessStatus(
                False,
                "Neplatná cesta",
                f"Cesta '{self.original_path}' není platnou cestou v systému",
                "Zkontrolujte, zda cesta neobsahuje nepovolené znaky"
            )
            return False

    def prepare_test_environment(self) -> bool:
        """Připraví testovací prostředí."""
        try:
            self.test_file = self.path.parent / "_config_test.json"
            self.path.parent.mkdir(parents=True, exist_ok=True)
            return True
        except PermissionError:
            self.status = SystemAccessStatus(
                False,
                "Nelze vytvořit adresář",
                f"Nemáte oprávnění vytvořit adresář v '{self.path.parent}'",
                "Zkontrolujte oprávnění nebo zvolte jinou cestu"
            )
            return False

    def create_test_file(self) -> bool:
        """Vytvoří testovací soubor."""
        try:
            self.test_file.touch()
            return True
        except PermissionError:
            self.status = SystemAccessStatus(
                False,
                "Nelze vytvořit soubor",
                f"Nemáte oprávnění vytvořit soubor '{self.test_file}'",
                "Zkontrolujte oprávnění k zápisu"
            )
            return False

    def write_test_data(self) -> bool:
        """Zapíše testovací data."""
        try:
            with self.test_file.open('w', encoding='utf-8') as f:
                json.dump(self.test_data, f)
            return True
        except PermissionError:
            self.status = SystemAccessStatus(
                False,
                "Nelze zapisovat do souboru",
                f"Nemáte oprávnění zapisovat do '{self.test_file}'",
                "Zkontrolujte oprávnění k zápisu"
            )
            return False

    def verify_test_data(self) -> bool:
        """Ověří přečtená data."""
        try:
            with self.test_file.open('r', encoding='utf-8') as f:
                read_data = json.load(f)

            if read_data == self.test_data:
                return True

            self.status = SystemAccessStatus(
                False,
                "Chyba integrity dat",
                "Přečtená data neodpovídají zapsaným datům",
                "Může jít o problém s diskem nebo právy"
            )
            return False
        except (PermissionError, json.JSONDecodeError):
            self.status = SystemAccessStatus(
                False,
                "Nelze číst data",
                f"Problém při čtení souboru '{self.test_file}'",
                "Zkontrolujte oprávnění ke čtení"
            )
            return False

    def cleanup(self) -> bool:
        """Uklidí testovací soubor."""
        try:
            if self.test_file.exists():
                self.test_file.unlink()
                if not self.test_file.exists():
                    return True
            self.status = SystemAccessStatus(
                False,
                "Nelze smazat soubor",
                f"Soubor '{self.test_file}' se nepodařilo smazat",
                "Zkontrolujte oprávnění nebo zda není soubor používán"
            )
            return False
        except PermissionError:
            self.status = SystemAccessStatus(
                False,
                "Nelze smazat soubor",
                f"Nemáte oprávnění smazat soubor '{self.test_file}'",
                "Zkontrolujte oprávnění k mazání"
            )
            return False

    def test(self) -> SystemAccessStatus:
        """Provede kompletní test systému."""
        # Reset statusu
        self.status = None

        # Postupné kroky testu
        steps = [
            self.validate_path,
            self.prepare_test_environment,
            self.create_test_file,
            self.write_test_data,
            self.verify_test_data,
            self.cleanup
        ]

        for step in steps:
            if not step():
                # Pokusíme se o úklid při selhání
                if self.test_file and self.test_file.exists():
                    try:
                        self.test_file.unlink()
                    except:
                        pass
                return self.status

        return SystemAccessStatus(
            True,
            "Systém je dostupný",
            f"Úspěšně otestován přístup k adresáři '{self.path.parent}'",
            ""
        )


# Ukázka použití:
def test_system_access(config_path: Union[Path, str]) -> SystemAccessStatus:
    """
    Pomocná funkce pro jednodušší použití SystemAccessTester.
    """
    tester = SystemAccessTester(config_path)
    return tester.test()