print("cli_styler/_styles_settings/styles_manager.py")
from ._error import ErrorStyle
from ._hint import HintStyle
from ._info import InfoStyle
from ._intro import IntroStyle
from ._menu import MenuStyle
from ._prompt import PromptStyle
from ._success import SuccessStyle
from ._warning import WarningStyle


class GetStyles:
    """Spravuje všechny styly CLI"""

    def __init__(self, colors, symbols):
        self.hint = HintStyle(colors, symbols)
        self.menu = MenuStyle(colors, symbols)
        self.prompt = PromptStyle(colors, symbols)


class CLIPrint:
    """Spravuje všechny styly CLI"""

    def __init__(self, colors, symbols):
        self.error = ErrorStyle(colors, symbols, display=True)
        self.info = InfoStyle(colors, symbols, display=True)
        self.intro = IntroStyle(colors, symbols, display=True)
        self.success = SuccessStyle(colors, symbols, display=True)
        self.warning = WarningStyle(colors, symbols, display=True)
