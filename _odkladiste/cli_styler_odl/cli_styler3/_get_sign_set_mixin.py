from abc import ABC

class GetSignSetMixin(ABC):
    """Spravuje znaky a nastavuje správnou variantu podle zvolené sady."""

    # Definice podporovaných sad znaků
    # (indexy odpovídají pořadí v seznamu znaků)
    SETS = {"set_a": 0, "set_b": 1, "native": 2}

    # Styly které se nemění
    NO_SIGN = ""
    END_LINE = " \n"
    EMPTY_LINE = "\n"

    def get_sign_set(self, sign_set):
        """
        Nastaví znaky podle vybrané sady.

        Metoda nejprve ověří, zda je zvolená sada podporovaná.
        - Pokud ne vyvolá výjimku.

        Následně dojde k získání indexu odpovídajícího vybrané sadě.
        Poté metoda projde seznam všech definovaných znaků z rodičovské třídy
        a uloží do atributů pouze jednu variantu odpovídající zvolené sadě.
        """

        # Ověření zvolené sady znaků a načtení indexu
        self.validate_sign_set(sign_set)
        set_index = self.SETS[sign_set]

        signs_set = {
            "INTRO"         : [" ■ ",   " ■ ",  ""],
            "INFO"          : [" ☐ ",   " ☐ ", ""],
            "LIST"          : [" - ",   " - ",  ""],
            "SUCCESS"       : [" ☑ ",   " ☑ ", ""],
            "DROPDOWN"      : [" ▼ ",   " ▼ ",  ""],
            "SELECTED"      : [" » ",   " » ",  ""],
            "UNSELECTED"    : ["   ",   "   ",  ""],
            "ERROR"         : [" ⛝ ",   " ⛝ ", ""],
            "WARNING"       : [" ⚠ ",   " ⚠ ",  ""]
        }

        signs_dict = {}
        for key, value in signs_set.items():
            signs_dict[key] = value[set_index]

        return signs_dict


    def validate_sign_set(self, sign_set):
        """Ověření zvolené sady znaků"""
        if sign_set not in self.SETS:
            raise ValueError(f"Neplatná sada znaků: {sign_set}")

