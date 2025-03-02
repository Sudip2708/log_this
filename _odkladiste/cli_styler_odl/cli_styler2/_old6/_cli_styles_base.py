from ..abc_helper import AbcSingletonMeta

class CLIStylesBase(metaclass=AbcSingletonMeta):
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
            self.set_style_attributes(signs, colors)
            self._initialized = True

    # Definice pro inicializaci
    def set_style_attributes(self, signs, colors):
        """Načte stylizované atributy na základě aktuálních sad."""

        # Defince stylů
        sgn, clr = signs, colors
        styles_definitions = {
            "intro_title"  : (sgn.INTRO, clr.BLUE + " bold reverse"),
            "intro_end"    : (sgn.NO_SIGN, clr.BLUE),
            "menu_title"   : (sgn.DROPDOWN, clr.DARK_GREEN + " bold reverse"),
            "menu_offer"   : (sgn.UNSELECTED, clr.LIGHT_GREEN),
            "menu_selected": (sgn.SELECTED, clr.GREEN + " bold reverse"),
            "error_title"  : (sgn.ERROR, clr.LIGHT_RED + " bold reverse"),
            "error_text"   : (sgn.LIST, clr.RED),
            "warning_title": (sgn.WARNING, clr.LIGHT_RED + " bold reverse"),
            "info_title"   : (sgn.INTRO, clr.LIGHT_PURPLE + " bold reverse"),
            "success_title": (sgn.SUCCESS, clr.BROWN + " bold reverse"),
            "prompt_input" : (sgn.SELECTED, clr.LAVENDER + " bold"),
        }

        # Přidání stylů do atributů
        for key, value in styles_definitions.items():
            setattr(self, key, value)

    @classmethod
    def get_styles(cls):
        """Vrátí seznam atributů obsahujících definice stylu."""
        return {
            key: value
            for key, value in cls.__dict__.items()
            if isinstance(value, tuple)
        }
