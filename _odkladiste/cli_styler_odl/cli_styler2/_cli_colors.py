from ._colors_base import ColorsBase
from ...abc_helper import AbcSingletonMeta

class CLIColors(ColorsBase, metaclass=AbcSingletonMeta):
    """Spravuje barvy a nastavuje správnou variantu podle zvoleného režimu."""

    # Definice podporovaných režimů
    # (indexy odpovídají pořadí v seznamu barev)
    MODES = {"dark": 0, "light": 1, "native": 2}

    # Definice singletonu
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.change_mode("dark")
            self._initialized = True

    # Definice pro inicializaci
    def change_mode(self, mode):
        """
        Nastaví barvy podle vybraného režimu.

        Metoda nejprve ověří, zda je zvolený režim podporovaný.
        - Pokud ne vyvolá výjimku.

        Následně dojde k získání indexu odpovídajícího vybranému režimu.
        Poté metoda projde seznam všech definovaných barev z rodičovské třídy
        a uloží do atributů pouze jednu barvu odpovídající zvolenému režimu.
        """

        # Ověření zvoleného režimu a načtení indexu
        self.validate_mode(mode)
        mode_index = self.MODES[mode]

        colors_set = {
            "LAVENDER"      : ["#d19bfe", "#d19bfe", ""],
            "PINK"          : ["#d270ba", "#d270ba", ""],
            "MAGENTA"       : ["#c95fbb", "#c95fbb", ""],
            "DARK_GREEN"    : ["#4f9d4f", "#4f9d4f", ""],
            "GREEN"         : ["#178f17", "#178f17", ""],
            "LIGHT_GREEN"   : ["#66cc66", "#66cc66", ""],
            "BLUE"          : ["#268bd2", "#268bd2", ""],
            "LIGHT_PURPLE"  : ["#bf7fff", "#bf7fff", ""],
            "PURPLE"        : ["#ab72dc", "#ab72dc", ""],
            "BROWN"         : ["#bb8940", "#bb8940", ""],
            "ORANGE"        : ["#f7a734", "#f7a734", ""],
            "RED"           : ["#bb4040", "#bb4040", ""],
            "LIGHT_RED"     : ["#e76b6b", "#e76b6b", ""]
        }

        # Přepsání atributů
        for key, value in colors_set.items():
            setattr(self, key, value[mode_index])

    def validate_mode(self, mode):
        """Metoda pro změnu režimu"""
        if mode not in self.MODES:
            raise ValueError(f"Neplatný režim: {mode}")

