print("cli_styler/_styles_settings/styles_manager.py")
from ._hint import HintStyle
from ._menu import MenuStyle
from ._prompt import PromptStyle

class GetStyles:
    """Spravuje všechny styly CLI"""

    def __init__(self, colors, symbols):
        self.hint = HintStyle(colors, symbols)
        self.menu = MenuStyle(colors, symbols)
        self.prompt = PromptStyle(colors, symbols)
