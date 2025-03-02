from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from._styles_settings import StylesManager, StyleBase


class StylePrinter:
    """Hlavní třída pro tisk stylovaných textů."""

    def __init__(self, style_manager: StylesManager):
        # Odkaz na `StylesManager`
        self._get_style = style_manager
        # Instance konkrétního stylu (např. `IntroStyle`)
        self._style_instance = None

    def __getattr__(self, attr):
        """Zpracuje požadovaný atribut podle aktuálního stavu instance."""
        if self._style_instance is None:
            # Načtení stylu
            return self._load_style_instance(attr)
        # Vrácení funkce pro tisk
        return self._get_styled_text_function(attr)

    def _load_style_instance(self, attr):
        """První průchod → Načte instanci stylu (např. `IntroStyle`)."""
        new_instance = getattr(self._get_style, attr, None)
        if isinstance(new_instance, StyleBase):
            # Uložíme přímo do `self`
            self._style_instance = new_instance
            # Vrátíme stejnou instanci místo nové
            return self

        raise AttributeError(f"Styl '{attr}' neexistuje.")

    def _get_styled_text_function(self, attr):
        """Druhý průchod → Vrátí funkci pro formátování a tisk."""
        if hasattr(self._style_instance, attr):
            # Vrací funkci, která okamžitě tiskne
            return lambda text: self._print_styled(attr, text)

        raise AttributeError(
            f"Atribut '{attr}' neexistuje "
            f"v '{self._style_instance.__class__.__name__}'."
        )

    def _print_styled(self, attr, text):
        """Pomocná metoda pro získání stylovaného textu a tisk."""
        styled_text = getattr(self._style_instance, attr)(text)
        self._style_instance = None
        print_formatted_text(FormattedText([styled_text]))
