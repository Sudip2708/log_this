# print("cli_styler/_styles_settings/_warning.py")
from ._base_calss import StyleBase, StyleItems


class WarningStyle(StyleBase):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["WARNING"],
            color=colors["LIGHT_RED"],
            style=self.BOLD + self.REVERSE,
            end_line=self.CONTINUE
        )

        self.text = StyleItems(
            symbol=symbols["LIST_ITEM"],
            color=colors["RED"],
            style=self.NONE,
            end_line=self.CONTINUE
        )

        self.direction = StyleItems(
            symbol=symbols["SELECTED"],
            color=colors["RED"],
            style=self.NONE,
            end_line=self.END_LINE
        )

