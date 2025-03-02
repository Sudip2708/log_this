from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from._styles_settings import StylesManager, StyleBase


class StylePrinter:
    """Hlavní třída pro tisk stylovaných textů."""

    def __init__(self, style_manager: StylesManager):
        self._get_style = style_manager  # Odkaz na `StylesManager`
        self._style_instance = None  # Instance konkrétního stylu (např. `IntroStyle`)

    def __getattr__(self, attr):
        """Zpracuje požadovaný atribut podle aktuálního stavu instance."""
        if self._style_instance is None:
            return self._load_style_instance(attr)  # 🛠 Načtení stylu
        return self._get_styled_text_function(attr)  # 🔥 Vrácení funkce pro tisk

    def _load_style_instance(self, attr):
        """První průchod → Načte instanci stylu (např. `IntroStyle`)."""
        new_instance = getattr(self._get_style, attr, None)
        if isinstance(new_instance, StyleBase):
            print(f"🔍 Načtena instance stylu: {new_instance.__class__.__name__}")
            self._style_instance = new_instance  # ✅ Uložíme přímo do `self`
            return self  # ✅ Vrátíme stejnou instanci místo nové

        raise AttributeError(f"Styl '{attr}' neexistuje.")

    def _get_styled_text_function(self, attr):
        """Druhý průchod → Vrátí funkci pro formátování a tisk."""
        if hasattr(self._style_instance, attr):
            print(f"🎨 Použití stylu: {attr} z {self._style_instance.__class__.__name__}")
            return lambda text: self._print_styled(attr, text)  # Vrací funkci, která okamžitě tiskne

        raise AttributeError(f"Atribut '{attr}' neexistuje v '{self._style_instance.__class__.__name__}'.")

    def _print_styled(self, attr, text):
        """Pomocná metoda pro získání stylovaného textu a tisk."""
        styled_text = getattr(self._style_instance, attr)(text)
        self._style_instance = None
        print(f"🖨 Tisk stylovaného textu: {styled_text}")
        print_formatted_text(FormattedText([styled_text]))
