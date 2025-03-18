from abc import ABC

from abc_helper import abc_property, abc_method



class LogThisManagerMethodsMixin(ABC):

    config_manager = abc_property("config_manager")


    def get_category_config_keys(self, category):
        """Metoda vrací klíče pro danou kateforii"""

        keys_data = self.config_manager.items_manager.KEYS_DATA
        outcome = []
        for key, value in keys_data.items():
            print("## key, value: ", key, value)
            print("## value.CATEGORY: ", value.CATEGORY)
            if value.CATEGORY == category:
                outcome.append(key)

        return outcome