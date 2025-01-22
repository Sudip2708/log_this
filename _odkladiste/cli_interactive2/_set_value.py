class InteractiveConfig:
    def __init__(self, config):
        self.config = config

    def select_key(self):
        """Umožňuje uživateli vybrat klíč pro nastavení hodnoty."""
        print("Výběr klíče pro nastavení jeho hodnoty\n")
        print("Hint:")
        print("- Klíč můžete buď zadat přímo, nebo pomocí šipek vyhledat a vybrat entrem.")
        print("\nDostupné klíče:")

        keys = list(self.config.keys_data.keys())
        for key in keys:
            description = self.config.keys_data[key].info
            print(f"  Nastavení pro '{key}' - {description}")

        while True:
            selected_key = input("\n> Zadejte klíč přímo nebo stiskněte Enter pro výběr: ").strip()
            if not selected_key:  # Interaktivní výběr
                # Simulace interaktivního výběru (v reálné aplikaci lze použít knihovnu jako curses)
                print("\nPoužívám první klíč jako příklad interaktivního výběru.")
                return keys[0]  # Vrátí první klíč jako příklad
            elif selected_key in self.config.keys_data:
                return selected_key  # Platný klíč
            else:
                print("Neplatný klíč. Zkuste to znovu nebo použijte seznam.")

    def select_value(self, key):
        """Umožňuje uživateli zadat hodnotu pro vybraný klíč."""
        key_data = self.config.keys_data[key]
        print(f"\nZadání nové hodnoty pro klíč '{key}':")
        print(f"\nOptions: {key_data.detail}")
        print(f"\nHint: {key_data.hint}")

        while True:
            value = input(f"> Zadejte hodnotu pro '{key}': ").strip()
            try:
                valid_value = key_data.validate(value)
                return valid_value  # Vrátí validní hodnotu
            except ValueError as e:
                print(f"Chyba: {e}. Zkuste zadat hodnotu znovu.")

    def set_value(self):
        """Nastaví hodnotu pro klíč v konfiguraci."""
        key = self.select_key()
        value = self.select_value(key)
        self.config[key] = value
        print(f"Hodnota '{value}' byla úspěšně nastavena pro klíč '{key}'.")
