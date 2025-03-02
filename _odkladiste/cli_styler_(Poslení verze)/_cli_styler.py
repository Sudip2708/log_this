from ._styles_settings import (
    ErrorStyle,
    HintStyle,
    InfoStyle,
    IntroStyle,
    MenuStyle,
    PromptStyle,
    SuccessStyle,
    WarningStyle,
)


class CliStyler:


    def __init__(self, colors, symbols):

        self.error = ErrorStyle(colors, symbols)
        self.hint = HintStyle(colors, symbols)
        self.info = InfoStyle(colors, symbols)
        self.intro = IntroStyle(colors, symbols)
        self.menu = MenuStyle(colors, symbols)
        self.prompt = PromptStyle(colors, symbols)
        self.success = SuccessStyle(colors, symbols)
        self.warning = WarningStyle(colors, symbols)


