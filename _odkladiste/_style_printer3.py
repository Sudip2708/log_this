from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from._styles_settings import StylesManager, StyleBase


class StyleProxy:
    """Proxy třída pro přesměrování volání na StylesManager a tisk."""

    def __init__(self, style_manager, style_path=None):
        self._style_manager = style_manager
        self._style_path = style_path or []  # Cesta ke stylu, např. ["intro", "title"]

    def __getattr__(self, attr):
        """Přidá další část cesty (např. .intro, .title)."""
        return StyleProxy(self._style_manager, self._style_path + [attr])

    def __call__(self, text: str):
        """Jakmile dojde k volání se stringem, zavoláme správnou metodu na StylesManager."""
        if not isinstance(text, str):
            raise TypeError("StylePrinter očekává pouze text (str).")

        # Dynamicky najdeme požadovaný styl v get_style
        style_obj = self._style_manager
        for attr in self._style_path:
            style_obj = getattr(style_obj, attr, None)

        if not isinstance(style_obj, StyleBase):
            raise AttributeError(f"Styl '{'.'.join(self._style_path)}' nebyl nalezen.")

        # Použijeme styl k formátování textu
        style_item = style_obj(text)
        print_formatted_text(FormattedText([style_item]))


class StylePrinter:
    """Hlavní třída pro tisk stylovaných textů."""

    def __init__(self, style_manager: StylesManager):
        self._style_manager = style_manager

    def __getattr__(self, attr):
        """Vytvoří proxy objekt pro styl (např. cli_print.intro.title)."""
        return StyleProxy(self._style_manager, [attr])
