import os


class GetConfigFilePathMixin:

    @classmethod
    def _get_config_file_path(cls, file_name: str='config.json') -> str:
        """
        Určí cestu ke konfiguračnímu souboru.

        Cestu určuje dle umístění souboru s definicí třídy.
        Konfigurační soubor tedy bude vždy na stejném umístění ,
        jako je soubor s definicí třídy LogThisConfig.

        Returns:
            str: Absolutní cesta ke konfiguračnímu JSON souboru
        """

        # Načtení cesty k souboru s kodem třídy
        config_dir = os.path.dirname(__file__)

        # Vrácení cesty s odkazen na config.json
        return os.path.join(config_dir, file_name)


