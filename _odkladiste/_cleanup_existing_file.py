"""
Závislosti:
- _config_path:
- delete_config_file:

"""

class CleanupExistingFileMixin:

    def _cleanup_existing_file(self) -> None:
        """Pokusí se smazat existující konfigurační soubor."""

        try:

            # Kontrola zda konfigurační soubor existuje
            if self._config_path.exists():

                # Volání funkce pro smazání souboru
                delete_config_file(self._config_path)

        Zachycení případných výjimek
        except DeleteConfigFileError as e:
            self._handle_delete_error(e)