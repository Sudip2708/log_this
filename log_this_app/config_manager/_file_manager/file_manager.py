from pathlib import Path
import json

from ._mixins import (
    CheckConfigFileDataMixin,
    SaveConfigurationMixin,
    GetConfigurationMixin
)

class ConfigFileManager(

    SaveConfigurationMixin,
    # Přidává metody: save_configuration()
    # Používá atributy: _cm

    CheckConfigFileDataMixin,
    # Přidává metody: _check_config_file_data(load_data)
    # Používá atributy: _cm
    # Používá metody: save_configuration()

    GetConfigurationMixin,
    # Přidává metody: get_configuration()
    # Používá atributy: _cm
    # Používá metody: _check_config_file_data()

):


    _cm = None
    _save = None

    def __init__(self, config_manager):

        # Načtení přístupu k hlavní třídě
        self._cm = config_manager

        # Vytvoření konfiguračního souboru
        self.save_configuration()





