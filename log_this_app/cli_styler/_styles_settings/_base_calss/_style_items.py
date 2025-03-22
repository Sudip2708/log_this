# print("cli_styler/_styles_settings/_base_calss/_style_items.py")
from dataclasses import dataclass


@dataclass
class StyleItems:
    symbol: str
    color: str
    style: str
    end_line: str

    def __call__(self, text: str) -> tuple:
        """Metoda navrací ostylovaný text jako tuple (style, text)"""
        return f"{self.color}{self.style}", f"{self.symbol}{text}{self.end_line}"

    # def __call__(self, *texts: str) -> tuple:
    #     """Metoda navrací ostylovaný text jako tuple (style, text)"""
    #
    #     if not isinstance(texts, tuple):
    #         texts = tuple(texts)
    #     outcome = []
    #     for text in texts:
    #         outcome.append((f"{self.color}{self.style}", f"{self.symbol}{text}{self.end_line}"))
    #     return outcome