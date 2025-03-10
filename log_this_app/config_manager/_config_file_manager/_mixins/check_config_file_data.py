from pathlib import Path
import json
from abc import ABC

from abc_helper import abc_property, abc_method

class CheckConfigFileDataMixin(ABC):

    _cm = abc_property("_cm")
    _save_configuration = abc_method("_save_configuration")


    def _check_config_file_data(
            self,
            load_data: dict
    ):
        """Metoda zkontroluje data z konfiguračního souboru

        Args:
            load_data (dict): Konfigurační data k ověření.

        Raises:
            ValueError: Pokud se nejedná a validní data.
            RuntimeError: Neočekávaná chyba.
        """

        # Ověření, zda načtená data jsou slovník
        if not isinstance(load_data, dict):
            raise TypeError(
                f"Očekáván typ dict, ale získán {type(load_data).__name__}"
            )

        try:

            # Vytvoření proměnné pro validační funkci před vykonáním přiřazení
            value_validation = self._cm.items_manager.value_validation
            default_values = self._cm.items_manager.default_values()

            # Vytvoření konfiguračního slovníku
            checked_data = {
                key: (
                    file_value
                    if value_validation(key, file_value := load_data.get(key))
                    else default_value
                )
                for key, default_value in default_values.items()
            }

            # Kontrola, zda je potřeba přepsat konfigurační soubor
            if checked_data != load_data:
                self._save_configuration(checked_data)

            # Navrácení slovníku obsahující klíč a hodnotu
            return checked_data


        except (TypeError, AttributeError, KeyError) as e:
            raise ValueError(
                f"Neplatná data v konfiguračním souboru: {e}") from e

        except Exception as e:
            raise RuntimeError(
                f"Neočekávaná chyba při kontrole konfigurace: {e}") from e
