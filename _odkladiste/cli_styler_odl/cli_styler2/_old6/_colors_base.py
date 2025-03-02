class ColorsBase:
    """Definuje všechny dostupné barvy a jejich varianty pro různé režimy."""

    # Název barvy   ["light", "dark", "default" ]
    LAVENDER        = ["#d19bfe", "#d19bfe", ""]
    PINK            = ["#d270ba", "#d270ba", ""]
    MAGENTA         = ["#c95fbb", "#c95fbb", ""]
    DARK_GREEN      = ["#4f9d4f", "#4f9d4f", ""]
    GREEN           = ["#178f17", "#178f17", ""]
    LIGHT_GREEN     = ["#66cc66", "#66cc66", ""]
    BLUE            = ["#268bd2", "#268bd2", ""]
    LIGHT_PURPLE    = ["#bf7fff", "#bf7fff", ""]
    PURPLE          = ["#ab72dc", "#ab72dc", ""]
    BROWN           = ["#bb8940", "#bb8940", ""]
    ORANGE          = ["#f7a734", "#f7a734", ""]
    RED             = ["#bb4040", "#bb4040", ""]
    LIGHT_RED       = ["#e76b6b", "#e76b6b", ""]

    @classmethod
    def get_all_colors(cls):
        """
        Vrátí všechny dostupné definice barev jako slovník.

        Prochází všechny atributy této třídy a vybírá pouze ty,
        které nejsou speciální (`__dunder__` metody) a obsahují seznam hodnot.

        Návratová hodnota:
            dict[str, list[str]]:
                - Klíč: název barvy jako řetězec (např. `"LAVENDER"`)
                - Hodnota: seznam barevných variant [dark, light, default]
        """
        return {
            attr: getattr(cls, attr)
            for attr in dir(cls)
            if not attr.startswith("_")
               and isinstance(getattr(cls, attr), list)
        }
