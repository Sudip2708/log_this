import logging


class ResetConfigMixin:


    def reset_config(self) -> None:
        """
        Resetuje konfiguraci na výchozí hodnoty.

        Metoda nejprve přepíše hodnoty v instančním slovníku.
        Nakonec metoda uloží hodnoty do konfiguračního souboru.
        Pokud se to nepovede, metoda načte zpět původní hodnoty.
        """

        # Nastavení konfigurace na defaultní hodnoty
        self.config = self.DEFAULTS.copy()

        # Uložení hodnot do konfiguračního souboru
        path = self._get_config_file_path()
        if not self._save_config_to_file(path, self.config):
            self._load_default_config()

        logging.info("Konfigurace byla resetována na výchozí hodnoty.")




def reset_config(self) -> None:
    """
    Resetuje konfiguraci na výchozí hodnoty.

    Metoda nejprve přepíše hodnoty v instančním slovníku.
    Nakonec metoda uloží hodnoty do konfiguračního souboru.
    Pokud se to nepovede, metoda načte zpět původní hodnoty.
    """

    # Nastavení konfigurace na defaultní hodnoty
    self.config = self.DEFAULTS.copy()

    # Uložení hodnot do konfiguračního souboru
    path = self._get_config_file_path()
    if not self._save_config_to_file(path, self.config):
        self._load_default_config()

    logging.info("Konfigurace byla resetována na výchozí hodnoty.")

class ConfigMixin:

    def reset_config(self) -> None:
        """Resetuje konfiguraci na výchozí hodnoty."""
        reset_config(self)