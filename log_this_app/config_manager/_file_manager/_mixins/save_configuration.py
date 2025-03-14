from pathlib import Path
import json
from abc import ABC


from abc_helper import abc_property

class SaveConfigurationMixin(ABC):

    _cm = abc_property("_cm")

    def save_configuration(
            self,
            config_dict: dict = None,
            path: Path = None,
    ):
        """Zapíše konfiguraci do souboru, pokud je to možné.

        Args:
            config_dict (dict): Konfigurační data k uložení.
            path (Path, optional): Cesta k souboru, kam se má uložit konfigurace.
                Pokud není zadána, použije se výchozí konfigurační soubor.

        Raises:
            ValueError: Chyba při serializaci JSON.
            PermissionError: Nedostatečná práva pro zápis.
            FileNotFoundError: Cesta ke konfiguračnímu souboru neexistuje.
            OSError: Obecná chyba při práci se souborem.
            RuntimeError: Neočekávaná chyba.
        """

        # Použití výchozí konfigurace a cesty, pokud není zadána jiná
        config_dict = config_dict or self._cm.items_manager.default_values()
        path = path or self._cm.CONFIG_FILE_PATH

        # Ověření, zda načtená data jsou slovník
        if not isinstance(config_dict, dict):
            raise TypeError(
                f"Očekáván typ dict, ale získán {type(config_dict).__name__}"
            )

        # Ověření, zda path je instancí Path
        if not isinstance(path, Path):
            raise TypeError(
                f"Očekáván typ {Path.__name__}, ale získán {type(path).__name__}")

        try:

            # Pokud soubor existuje, dojde k jeho smazání
            if path.exists():
                path.unlink()

            # Zápis do souboru
            with path.open("w", encoding="utf-8") as file:
                json.dump(config_dict, file, indent=4, ensure_ascii=False)  # type: ignore


        except (TypeError, OverflowError) as e:
            raise ValueError(
                f"Chyba při serializaci JSON dat: {e}"
            ) from e

        except PermissionError as e:
            raise PermissionError(
                f"Nedostatečná práva pro zápis do {path}"
            ) from e

        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"Cesta ke konfiguračnímu souboru neexistuje: {path}"
            ) from e

        except OSError as e:
            raise OSError(
                f"Chyba při práci se souborem {path}: {e}"
            ) from e

        except Exception as e:
            raise RuntimeError(
                f"Neočekávaná chyba při ukládání JSON souboru: {e}"
            ) from e


