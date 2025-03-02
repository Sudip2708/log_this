from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from._styles_settings import StylesManager, StyleBase


class StylePrinter:
    """Hlavní třída pro tisk stylovaných textů."""

    def __init__(self, style_manager, style_instance=None, _style_attribute_name=None):
        self._get_style = style_manager
        self._style_path = style_path or []

    def __getattr__(self, attr):
        """Umožní volání `cli_print.xxx` a `cli_print.xxx.yyy`."""
        return StylePrinter(self._get_style, self._style_path + [attr])

    def __call__(self, text: str):
        """Najde styl podle cesty a použije ho na text."""
        try:
            # Vyhledání stylu podle _style_path
            style = self._get_style
            for attr in self._style_path:
                print(f"🔍 Hledám '{attr}' v objektu {style.__class__.__name__}")
                style = getattr(style, attr)  # Navigace v `StylesManager`

            # Ověření, že nalezený styl je instance StyleBase
            if not isinstance(style, StyleBase):
                raise AttributeError(f"Styl '{'.'.join(self._style_path)}' není platný.")

            # Použití stylu na text (StyleBase má __call__ metodu)
            styled_text = style(text)

            # Vytisknutí ostylovaného textu
            print_formatted_text(FormattedText([styled_text]))

        except AttributeError as e:
            print(f"Chyba: {e}")  # Ladící výstup pro odhalení chyb