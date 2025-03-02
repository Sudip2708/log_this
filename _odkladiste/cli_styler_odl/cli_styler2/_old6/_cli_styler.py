from ..abc_helper import AbcSingletonMeta
from .signs.cli_sings import END_LINE


class CLIStyler(metaclass=AbcSingletonMeta):
    """Dědí z CLIDataClass a přidává generování ostylovaného textu."""

    # Definice singletonu
    def __init__(self, styles):
        if not hasattr(self, "_initialized"):
            self.set_styler_attributes(styles)
            self._initialized = True

    # Nastavení atributů
    def set_styler_attributes(self, styles):
        for key, (symbol, style) in styles.get_styles().items():
            setattr(self, key,
                    lambda text, s=symbol, st=style:
                    self.get_styled_text(s, st, text))

    # Hlavní metoda pro navrácení stylu
    @staticmethod
    def get_styled_text(symbol: str, style: str, text: str) -> tuple:
        """Vrátí tuple obsahující styl a ostylovaný text."""
        return style, f"{symbol}{text}{END_LINE}"


    @classmethod
    def get_styles(cls):
        """Vrátí seznam atributů obsahujících definice stylu."""
        return {
            key: value
            for key, value in cls.__dict__.items()
            if isinstance(value, tuple)
        }