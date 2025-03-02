from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from ._styles_settings import StylesManager, StyleBase


class StylePrinter:
    """Hlavní třída pro tisk stylovaných textů."""

    def __init__(self, style_manager: StylesManager, style_instance=None):
        self._get_style = style_manager  # Odkaz na `StylesManager`
        self._style_instance = style_instance  # Např. `IntroStyle`

    def __getattr__(self, attr):
        """Vyhledá instanci stylu nebo rovnou zavolá atribut stylu."""
        if self._style_instance is None:
            # 🛠 První průchod → Hledáme instanci stylu (např. `intro`)
            new_instance = getattr(self._get_style, attr, None)
            if isinstance(new_instance, StyleBase):
                print(
                    f"🔍 Načtena instance stylu: {new_instance.__class__.__name__}")
                return StylePrinter(self._get_style,
                                    style_instance=new_instance)
            else:
                raise AttributeError(f"Styl '{attr}' neexistuje.")

        else:
            # 🔥 Druhý průchod → Rovnou zavoláme metodu pro tisk
            if hasattr(self._style_instance, attr):
                print(
                    f"🎨 Použití stylu: {attr} z {self._style_instance.__class__.__name__}")
                return lambda text: self._print_styled(attr,
                                                       text)  # Vrací funkci, která okamžitě tiskne
            else:
                raise AttributeError(
                    f"Atribut '{attr}' neexistuje v '{self._style_instance.__class__.__name__}'.")

    def _print_styled(self, attr, text):
        """Pomocná metoda pro získání stylovaného textu a tisk."""
        styled_text = getattr(self._style_instance, attr)(text)
        print(f"🖨 Tisk stylovaného textu: {styled_text}")
        print_formatted_text(FormattedText([styled_text]))

    def __call__(self, text: str):
        """Přímý tisk bez stylu (může být nahrazen výchozím stylem)."""
        print(f"📝 Přímý tisk textu: {text}")
        print_formatted_text(FormattedText([("", text)]))
