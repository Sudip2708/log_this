# print("cli_styler/_styles_settings/_success.py")
from ._base_calss import StyleBase, StyleItems


class SuccessStyle(StyleBase):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["ERROR"],
            color=colors["LIGHT_RED"],
            style=self.BOLD + self.REVERSE,
            end_line=self.END_LINE
        )

        self.text = StyleItems(
            symbol=symbols["LIST_ITEM"],
            color=colors["RED"],
            style=self.BOLD + self.REVERSE,
            end_line=self.CONTINUE
        )
