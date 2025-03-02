from ..abc_helper import AbcSingletonMeta


class CLIStyler(metaclass=AbcSingletonMeta):
    """
    Základní třída uchovávající styly pro CLI aplikaci.

    Každý atribut definuje styl textu kombinací:
        - znaku (převzatého z `CLISigns`)
        - barvy a formátování (převzatého z `CLIColors`)

    Používá singleton vzor, aby byla zajištěna konzistence v celé aplikaci.
    """

    # Definice singletonu
    def __init__(self, signs, colors):
        if not hasattr(self, "_initialized"):
            self._styles_keys = []
            self.set_styler_attributes(signs, colors)
            self._initialized = True

    # Nastavení atributů
    def set_styler_attributes(self, signs, colors):

        # Defince stylů
        s, c = signs, colors
        styles_definitions = {
            "intro_title"  : (s["INTRO"], c["BLUE"] + " bold reverse"),
            "intro_end"    : (s["NO_SIGN"], c["BLUE"]),
            "menu_title"   : (s["DROPDOWN"], c["DARK_GREEN"] + " bold reverse"),
            "menu_offer"   : (s["UNSELECTED"], c["LIGHT_GREEN"]),
            "menu_selected": (s["SELECTED"], c["GREEN"] + " bold reverse"),
            "error_title"  : (s["ERROR"], c["LIGHT_RED"] + " bold reverse"),
            "error_text"   : (s["LIST"], c["RED"]),
            "warning_title": (s["WARNING"], c["LIGHT_RED"] + " bold reverse"),
            "info_title"   : (s["INTRO"], c["LIGHT_PURPLE"] + " bold reverse"),
            "success_title": (s["SUCCESS"], c["BROWN"] + " bold reverse"),
            "prompt_input" : (s["SELECTED"], c["LAVENDER"] + " bold"),
        }

        for key, (symbol, style) in styles_definitions.items():
            self._styles_keys.append(key)
            setattr(self, key,
                    lambda text, sy=symbol, st=style:
                    self.get_styled_text(sy, st, text))

    # Hlavní metoda pro navrácení stylu
    @staticmethod
    def get_styled_text(symbol: str, style: str, text: str) -> tuple:
        """Vrátí tuple obsahující styl a ostylovaný text."""
        return style, f"{symbol}{text} \n"


    def get_styles_keys(self):
        """Vrátí seznam řetězců s názvy atributů pro definování stylu."""
        return self._styles_keys