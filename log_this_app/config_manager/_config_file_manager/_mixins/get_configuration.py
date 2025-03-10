from pathlib import Path
import json
from abc import ABC

from abc_helper import abc_property, abc_method

class GetConfigurationMixin(ABC):

    _cm = abc_property("_cm")
    _check_config_file_data = abc_method("_check_config_file_data")


    def get_configuration(
            self,
            path: Path = None,
    ):
        """Načte konfiguraci z JSON souboru.

        Tato metoda načte konfiguraci z JSON souboru na zadané cestě, pokud není cesta zadána,
        použije se výchozí cesta definovaná v `self._cm.CONFIG_FILE_PATH`. Po načtení souboru
        provede kontrolu dat a vrátí je.

        Args:
            path (Path, optional): Cesta k souboru, ze kterého se má načíst konfigurace.
                Pokud není zadána, použije se výchozí cesta.

        Returns:
            dict: Načtená a validní konfigurace.

        Raises:
            ValueError: Chyba při dekódování JSON souboru, například pokud je soubor poškozený.
            FileNotFoundError: Soubor na zadané cestě neexistuje.
            PermissionError: Nedostatečná práva pro čtení souboru.
            OSError: Obecná chyba při práci se souborem, například problémy s přístupem k souboru.
            RuntimeError: Neočekávaná chyba při načítání souboru nebo dat.
        """

        # Použití výchozí cesty, pokud není zadána jiná
        path = path or self._cm.CONFIG_FILE_PATH

        # Ověření, zda path je instancí Path
        if not isinstance(path, Path):
            raise TypeError(
                f"Očekáván typ {Path.__name__}, ale získán {type(path).__name__}")

        try:

            # Načtení, kontrola a navrácení dat ze souboru
            with path.open('r', encoding='utf-8') as file:
                return self._check_config_file_data(json.load(file))


        except json.JSONDecodeError as e:
            raise ValueError(
                f"Chyba při dekódování JSON souboru: {e}"
            ) from e

        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Soubor nebyl nalezen na cestě: {path}"
            ) from e

        except PermissionError as e:
            raise PermissionError(
                f"Nedostatečná práva pro čtení souboru {path}"
            ) from e

        except OSError as e:
            raise OSError(
                f"Chyba při práci se souborem {path}: {e}"
            ) from e

        except Exception as e:
            raise RuntimeError(
                f"Neočekávaná chyba při načítání JSON souboru: {e}"
            ) from e
