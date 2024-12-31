from .mixins_data import (
    ConfigConstants,
    ensure_config_file,
    validate_and_update_config
)

class ConfigLoaderMixin:
    """
    Mixin pro automatické načítání a validaci konfigurace.

    Poskytuje generickou metodu pro načítání konfigurace z JSON souboru
    s podporou validace a aktualizace konfiguračních hodnot.
    """

    @classmethod
    def _load_config(cls, config_path):
        """
        Načte a aktualizuje konfiguraci.

        Kroky:
        1. Zajistí existenci konfiguračního souboru
        2. Validuje konfiguraci
        3. Aktualizuje atributy třídy podle načtené konfigurace

        Args:
            config_path (str): Cesta ke konfiguračnímu souboru
        """

        # Zajištění souboru a načtení konfigurace
        config_data = ensure_config_file(
            config_path,
            ConfigConstants.DEFAULT_CONFIG
        )

        # Validace a aktualizace konfigurace
        updated_config = validate_and_update_config(
            config_data,
            ConfigConstants.DEFAULT_CONFIG
        )

        # Aktualizace mapování hodnot
        cls.values.update({
            'skip_this': updated_config['skip_this'],
            'one_line': updated_config['one_line'],
            'simple': updated_config['simple'],
            'detailed': updated_config['detailed'],
            'report': updated_config['report'],
            True: updated_config['true'],
            False: updated_config['false'],
            None: updated_config['none'],
            '': updated_config['empty'],
        })

        # Nastavení dalších parametrů
        cls.indent = updated_config['indent']
        cls.blank_lines = updated_config['blank_lines']
        cls.docstring_lines = updated_config['docstring_lines']
        cls.max_depth = updated_config['max_depth']