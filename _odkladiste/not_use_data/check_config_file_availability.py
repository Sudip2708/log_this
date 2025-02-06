from pathlib import Path
from typing import Tuple
from dataclasses import dataclass


@dataclass
class ConfigFileStatus:
    is_available: bool
    message: str
    detail: str = ""
    hint: str = ""


class ConfigFileAccessError(Exception):
    def __init__(self, message: str, detail: str = "", hint: str = ""):
        self.message = message
        self.detail = detail
        self.hint = hint
        super().__init__(self.message)


def check_config_file_availability(config_path: Path) -> ConfigFileStatus:
    """
    Ověří dostupnost a práva konfiguračního souboru.

    Args:
        config_path: Cesta ke konfiguračnímu souboru

    Returns:
        ConfigFileStatus: Objekt obsahující informace o dostupnosti souboru
    """
    try:
        # Pokud soubor existuje, zkontrolujeme práva
        if config_path.exists():
            if not config_path.is_file():
                return ConfigFileStatus(
                    False,
                    "Konfigurační cesta není soubor",
                    f"Cesta {config_path} existuje, ale není to soubor",
                    "Zadejte prosím cestu k souboru"
                )

            # Kontrola práv ke čtení
            try:
                with config_path.open('r') as f:
                    pass
            except PermissionError:
                return ConfigFileStatus(
                    False,
                    "Nelze číst konfigurační soubor",
                    f"Nemáte práva ke čtení souboru {config_path}",
                    "Zkontrolujte oprávnění souboru"
                )

            # Kontrola práv k zápisu
            try:
                with config_path.open('a') as f:
                    pass
            except PermissionError:
                return ConfigFileStatus(
                    False,
                    "Nelze zapisovat do konfiguračního souboru",
                    f"Nemáte práva k zápisu do souboru {config_path}",
                    "Zkontrolujte oprávnění souboru"
                )

            return ConfigFileStatus(
                True,
                "Konfigurační soubor je dostupný",
                f"Soubor {config_path} existuje a máte k němu plná práva"
            )

        # Pokud soubor neexistuje, zkusíme vytvořit
        else:
            try:
                # Zkontrolujeme, zda můžeme vytvořit adresáře
                config_path.parent.mkdir(parents=True, exist_ok=True)

                # Zkusíme vytvořit soubor
                config_path.touch()
                config_path.unlink()  # Smažeme testovací soubor

                return ConfigFileStatus(
                    True,
                    "Konfigurační soubor lze vytvořit",
                    f"Soubor {config_path} bude vytvořen při první změně konfigurace"
                )

            except PermissionError:
                return ConfigFileStatus(
                    False,
                    "Nelze vytvořit konfigurační soubor",
                    f"Nemáte práva k vytvoření souboru v {config_path.parent}",
                    "Zkontrolujte oprávnění adresáře nebo zvolte jinou cestu"
                )

    except Exception as e:
        return ConfigFileStatus(
            False,
            "Neočekávaná chyba při kontrole konfiguračního souboru",
            str(e),
            "Kontaktujte vývojáře"
        )