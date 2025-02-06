import json
from pathlib import Path
from dataclasses import dataclass
from typing import Union


@dataclass
class SystemAccessStatus:
    """Třída reprezentující výsledek testu přístupu k systému."""
    is_available: bool
    message: str
    detail: str = ""
    hint: str = ""


def test_system_access(config_path: Union[Path, str]) -> SystemAccessStatus:
    """
    Otestuje dostupnost systému pomocí vytvoření testovacího JSON souboru.

    Args:
        config_path: Cesta ke konfiguračnímu souboru (použije se jen pro získání adresáře)

    Returns:
        SystemAccessStatus: Objekt obsahující výsledek testu a případné chybové zprávy
    """
    try:
        # Převod na Path objekt, pokud dostaneme string
        config_path = Path(config_path)

        # Kontrola validity cesty
        try:
            config_path = config_path.resolve(strict=False)
        except RuntimeError:
            return SystemAccessStatus(
                False,
                "Neplatná cesta",
                f"Cesta '{config_path}' není platnou cestou v systému",
                "Zkontrolujte, zda cesta neobsahuje nepovolené znaky"
            )

        # Získání adresáře a vytvoření cesty k testovacímu souboru
        test_dir = config_path.parent
        test_file = test_dir / "_config_test.json"

        # Pokus o vytvoření adresářů, pokud neexistují
        try:
            test_dir.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            return SystemAccessStatus(
                False,
                "Nelze vytvořit adresář",
                f"Nemáte oprávnění vytvořit adresář v '{test_dir}'",
                "Zkontrolujte oprávnění nebo zvolte jinou cestu"
            )

        # Test vytvoření souboru
        try:
            # Testovací data
            test_data = {"test": "data"}

            # Zápis do souboru
            with test_file.open('w', encoding='utf-8') as f:
                json.dump(test_data, f)

            # Kontrola čtení
            with test_file.open('r', encoding='utf-8') as f:
                read_data = json.load(f)

            # Ověření dat
            if read_data != test_data:
                return SystemAccessStatus(
                    False,
                    "Chyba integrity dat",
                    "Přečtená data neodpovídají zapsaným datům",
                    "Může jít o problém s diskem nebo právy"
                )

            # Pokus o smazání
            test_file.unlink()

            # Kontrola že soubor byl skutečně smazán
            if test_file.exists():
                return SystemAccessStatus(
                    False,
                    "Nelze smazat soubor",
                    f"Soubor '{test_file}' se nepodařilo smazat",
                    "Zkontrolujte oprávnění nebo zda není soubor používán"
                )

            return SystemAccessStatus(
                True,
                "Systém je dostupný",
                f"Úspěšně otestován přístup k adresáři '{test_dir}'",
                ""
            )

        except PermissionError as e:
            # Pokus o úklid
            if test_file.exists():
                try:
                    test_file.unlink()
                except:
                    pass

            return SystemAccessStatus(
                False,
                "Nedostatečná oprávnění",
                f"Chyba při práci se souborem: {str(e)}",
                "Zkontrolujte oprávnění k zápisu a čtení"
            )

        except json.JSONDecodeError:
            # Pokus o úklid
            if test_file.exists():
                try:
                    test_file.unlink()
                except:
                    pass

            return SystemAccessStatus(
                False,
                "Chyba při práci s JSON",
                "Nelze číst/zapisovat JSON data",
                "Může jít o problém s kódováním nebo poškozený disk"
            )

    except Exception as e:
        return SystemAccessStatus(
            False,
            "Neočekávaná chyba",
            str(e),
            "Kontaktujte vývojáře"
        )


# Ukázka použití:
def initialize_config(config_path: Path) -> None:
    # Nejdřív otestujeme systém
    system_status = test_system_access(config_path)

    if not system_status.is_available:
        cli_print(
            style="error",
            info=system_status.message,
            detail=system_status.detail,
            hint=system_status.hint
        )
        # Zde by následovala logika pro práci bez konfiguračního souboru
        return

    # Pokud je systém dostupný, můžeme pokračovat s kontrolou
    # samotného konfiguračního souboru...