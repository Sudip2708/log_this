from abc import ABC

class CheckStyleAttributesMixin(ABC):

    def check_style_attributes(self, styles_dict):
        """
        Metoda pro kontzolu atributů

        # Získáme seznam atributů třídy (jen ty, které jsou relevantní)
        # Seznam dostupných stylů ve slovníku
        # Kontrola zda se shodují
        """
        attributes_set = self.get_style_attributes_set()
        styles_set = set(styles_dict.keys())
        if attributes_set != styles_set:
            self.raise_attributes_error(attributes_set, styles_set)

    def get_style_attributes_set(self):
        """
        Metoda pro vytvoření množiny atributů pro styly definované v této třídě

        # Načtení třídních metod a atributů
        # Odstranění atributů začínajících podtržítkem
        # Ujistíme se, že `init` není součástí
        """
        return {key for key in dir(self)
                if not key.startswith("_")
                and key != "init"}

    @staticmethod
    def raise_attributes_error(attributes_set, styles_set):
        message = "Neshoda mezi definovanými styly a atributy třídy CLIStyler\n"
        excess = attributes_set - styles_set
        message += f"Nadytečné atributy třídy CLIStyler: {excess}\n" if excess else ""
        missing = styles_set - attributes_set
        message += f"Chybějící atributy třídy CLIStyler: {missing}\n" if missing else ""
        raise ValueError(message)


