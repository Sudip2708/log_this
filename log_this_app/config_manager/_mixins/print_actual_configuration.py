from abc import ABC

from cli_styler import styler
from abc_helper import abc_property


class PrintActualConfigurationMixin(ABC):

    config = abc_property("config")
    items_manager = abc_property("items_manager")


    def print_actual_configuration(self, with_descriptions = False):

        # Když jde o požadavek na jednoduchý výpis
        if not with_descriptions:
            items_list = []
            for key, value in self.config.items():
                items_list.append(f"{key} - {value}")

        # Když jde o požadavek na výpis s podrobnostna
        else:
            items_list = []
            for key, value in self.config.items():
                items_list.append(f"{key} - {value}")
                items_list.append(f"{self.items_manager.KEYS_DATA[key].INFO}")
                items_list.append(f"{self.items_manager.KEYS_DATA[key].OPTIONS}")
                items_list.append(f"")