# print("cli_styler/_styles_settings/_intro.py")
from ._base_calss import StyleBase, StyleItems


class IntroStyle(StyleBase):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["INTRO"],
            color=colors["BLUE"],
            style=self.BOLD + self.REVERSE,
            end_line=self.END_LINE,
        )

        self.end = StyleItems(
            symbol=self.NONE,
            color=colors["BLUE"],
            style=self.NONE,
            end_line=self.END_LINE,
        )


