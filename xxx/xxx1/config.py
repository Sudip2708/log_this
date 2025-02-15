class Config:
    """Třída pro správu konfigurace"""

    def __init__(self):
        self.settings = {
            "key1": "value1",
            "key2": "value2"
        }

    def get_value(self, key):
        return self.settings.get(key)

    def set_value(self, key, value):
        self.settings[key] = value

    def print_configuration(self):
        print("Aktuální konfigurace:")
        for key, value in self.settings.items():
            print(f"{key}: {value}")
