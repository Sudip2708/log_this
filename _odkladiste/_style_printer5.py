from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from ._styles_settings import StylesManager, StyleBase


class StylePrinter:
    """Hlavní třída pro tisk stylovaných textů."""

    def __init__(self, style_manager: StylesManager, style_instance=None,
                 style_attribute_name=None):
        self._get_style = style_manager  # Odkaz na `StylesManager`
        self._style_instance = style_instance  # Např. `IntroStyle`
        self._style_attribute_name = style_attribute_name  # Např. `title`

    def __getattr__(self, attr):
        """Vyhledá instanci stylu nebo atribut stylu."""
        if self._style_instance is None:
            # První volání → Hledáme instanci stylu (např. `intro`)
            new_instance = getattr(self._get_style, attr, None)
            if isinstance(new_instance, StyleBase):
                print(
                    f"🔍 Načtena instance stylu: {new_instance.__class__.__name__}")
                return StylePrinter(self._get_style,
                                    style_instance=new_instance)
            else:
                raise AttributeError(f"Styl '{attr}' neexistuje.")

        else:
            # Druhé volání → Hledáme atribut stylu (např. `title`)
            if hasattr(self._style_instance, attr):
                print(f"🎨 Načten atribut stylu: {attr} z {self._style_instance.__class__.__name__}")
                return StylePrinter(self._get_style,
                                    style_instance=self._style_instance,
                                    style_attribute_name=attr)
            else:
                raise AttributeError(
                    f"Atribut '{attr}' neexistuje v '{self._style_instance.__class__.__name__}'.")

    def __call__(self, text: str):
        """Aplikuje styl na text a vytiskne ho."""
        if self._style_instance is None or self._style_attribute_name is None:
            raise AttributeError("StylePrinter nebyl správně inicializován.")

        # Získání stylované hodnoty
        styled_text = getattr(self._style_instance, self._style_attribute_name)(
            text)

        print(f"🖨 Tisk stylovaného textu: {styled_text}")
        print_formatted_text(FormattedText([styled_text]))
