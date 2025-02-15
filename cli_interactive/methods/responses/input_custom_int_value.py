from abc import ABC

from abc_helper import abc_property, abc_method

class InputCustomIntValueMixin(ABC):

    # Atribut zaznamenávající požadavek z interaktivního menu
    response = abc_property("response")

    # Atribut pro zaznamenání vybraného klíče
    selected_key = abc_property("selected_key")

    # Atribut pro zaznamenání vybrané hodnoty pro daný klíče
    selected_value = abc_property("selected_key")

    # Metoda která přepne menu na nové menu
    display_menu = abc_method("display_menu")

    # Metoda načte a zobrazí aktuální nabídku interaktivního menu
    run_menu = abc_method("run_menu")

    def input_custom_int_value(self):
        """Metoda umožňující ruční zadání int hodnoty (0 - 1000)"""

        # Intro text
        print(f"Ruční zadání hodnoty pro klíč '{self.selected_key}'")
        print("Povolené hodnoty: celé číslo v rozmezí 0 - 1000")
        print("(Pro návrat bez zadání ponechte prázdné pole a stiskněte Enter.)\n")

        # Cyklus pro zadání hodnoty
        while True:

            # Zadání hodnoty (změnít input na promp a nastylovat)
            selected_value = input("Zadejte hodnotu: ")

            # Kontrola zda nebyla zadaná žádná hodnota (pro opuštění zadání)
            # Pokud ano, dojde k přerušení cyklu
            if not selected_value:
                break

            # Kontrola zda je hodnota číslem mezi 0 - 1000
            # Pokud ano, dojde k přerušení cyklu
            try:
                if 0 <= int(selected_value) <= 1000:
                    break

            # Pokud kontrola byla zadaná nevalidní hodnota
            # Vypíše se oznam a znovu se nabídne možnost zadání
            except ValueError:
                print()
                print(f"Nesprávně zadaná hodnota: '{selected_value}'")
                print("Hodnota musí být celé číslo v rozsahu 0–1000")
                print("Zkuste to ještě jednou.")
                print()

        # Kontrola zda byla zadaná hodnota
        # Vytiskne prázdný řádek
        # Nastaví atributu 'selected_value' na danou hodnotu
        # Nastaví atributu 'response' na vytištění výsledku
        if selected_value:
            print()
            self.selected_value = selected_value
            self.response = "print_new"

        # Pokud nebyla zadaná žádná hodnota (pro opuštění zadání)
        # Vypíše se oznam o návratu do menu pro výběr hodnoty
        # Zavolá se metoda pro zobrazení menu
        else:
            print()
            print("Nebyla zadaná žádná hodnota. ")
            print("Návrat do menu pro výběr hodnoty. ")
            print()
            self.display_menu("select_value_menu")
            self.run_menu()
