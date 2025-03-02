from ._methods_mixin import StylePrinterMethodsMixin


class CLIPrint(

    StylePrinterMethodsMixin
    # Mixin s interními metodami pro vytištění stylovaného textu
    # Přidává metody: _load_style_instance(attr), _print_styled_text(attr), _execute_print(attr, text)
    # Používá atributy: _style_instance, _get_style

):
    """Spravuje všechny styly CLI a umožňuje tisknout stylované texty."""

    # Atribut pro dočasné umístění instance stylu
    _style_instance = None

    def __init__(self, get_style):
        # Načtení instance StylesManager pro získání stylu
        self._get_style = get_style


    def __getattr__(self, attr):
        """Dynamicky zpracuje požadovaný atribut."""

        # První průchod pro načtení instance stylu
        if self._style_instance is None:
            return self._load_style_instance(attr)

        # Druhý průchod pro vytištění stylovaného textu
        return self._print_styled_text(attr)


