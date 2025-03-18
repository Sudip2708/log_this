from abc import ABC

from cli_styler import styler
from abc_helper import abc_property, abc_method
from .._items_manager import CONFIG_CATEGORY

class PrintActualConfigurationMixin(ABC):

    config = abc_property("config")
    items_manager = abc_property("items_manager")
    get_value_meaning = abc_method("get_value_meaning")


    # def print_actual_configuration(self):
    #     """Metoda prostručný výpis aktuálně nastavených hodnot"""
    #
    #     # Vytištění nadpisu
    #     styler.cli_print.info.title("Aktuální konfigurace:")
    #
    #     # Vytvoření dalších položek
    #     items_list = []
    #     for key, value in self.config.items():
    #         value_meaning = self.get_value_meaning(key, value)
    #         items_list.append(f"{key} - {value} - {value_meaning}")
    #
    #     # Výpis možností
    #     styler.cli_print.info.text(*items_list)


    def print_actual_configuration2(self):
        """Metoda prostručný výpis aktuálně nastavených hodnot"""

        # Vytištění nadpisu
        styler.cli_print.info.title("Aktuální konfigurace:")

        # Vytvoření dalších položek (řazeno dle kategorií)
        items_list = []
        for category_key, value in CONFIG_CATEGORY.items():
            items_list.append("")  # Prázdné místo
            items_list.append(f"{value.upper()}:")

            # Načtení slovníku s položkami dané kategorie
            category_dict = self.items_manager.get_key_class_for_category(category_key)
            for key, key_class in category_dict.items():
                actual_value = self.config[key]
                value_meaning = self.get_value_meaning(key, actual_value)
                items_list.append(f"• {key} [{actual_value}] {value_meaning}")

        # Výpis možností
        styler.cli_print.info.text_blank(*items_list)



    def print_category_configuration(self, category):
        """Metoda pro vytištění podrobných informací ke kategoriím"""

        #Ověření platnosti kategorie
        if not category in CONFIG_CATEGORY.keys():
            raise ValueError(f"Byla zadaná neplatná kategorie: {category}")

        # Vytištění nadpisu
        styler.cli_print.info.title(f"Položky pro {CONFIG_CATEGORY[category].lower()}:")

        # Načtení slovníku s položkami dané kategorie
        category_dict = self.items_manager.get_key_class_for_category(category)

        # Vytvoření dalších položek
        items_list = []
        for key, key_class in category_dict.items():

            # Prázdný řádek
            items_list.append("")

            # Název klíče
            items_list.append(f"Klíč: {key}")

            # Informace o klíči
            items_list.append(f"Popis: {key_class.INFO}")

            # Aktuálně zvolená hodnota
            actual_value = self.config[key]
            value_meaning = self.get_value_meaning(key, actual_value)
            items_list.append(f"Aktuálně nastaveno: {actual_value} - {value_meaning}")

            # Výpis možností
            items_list.append(f"Možnosti:")
            for key_option, meaning in key_class.VALUES_DICT.items():
                default = key_option == key_class.DEFAULT_VALUE
                is_default = " (defaultní hodnota)" if default else ""
                items_list.append(f"• {key_option} - {meaning}{is_default}")

        # Výpis možností
        styler.cli_print.info.text_blank(*items_list)
