import os
import logging
from datetime import datetime
from typing import Optional

class ExportConfigToFileMixin:


    def export_config_to_file(
            self,
            export_path: Optional[str] = None
    ) -> str:
        """
        Exportuje aktuální konfiguraci do samostatného souboru.

        Args:
            export_path (Optional[str]): Cesta pro export konfigurace.
                                         Pokud není zadána, použije se výchozí umístění.

        Returns:
            str: Cesta k exportovanému konfiguračnímu souboru
        """


        # Pokud není definovaná cesta
        if not export_path:

            # Vytvoření jména souboru
            file_name = (f'config_export_'
                         f'{datetime.now().strftime("%Y%m%d_%H%M%S")}_'
                         f'{os.getpid()}.json')

            # Vytvoření cesty k souboru
            export_path = self._get_config_file_path(file_name)


        try:

            # Uložení souboru a vrácení cesty
            self._save_config_to_file(export_path, self.config)
            return export_path

        except Exception as e:
            logging.error(f"Chyba při exportu konfigurace: {e}")
            raise