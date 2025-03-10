# print("cli_styler/_styles_settings/_success.py")
from ._base_calss import StyleBase, StyleItems


class SuccessStyle(StyleBase):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["SUCCESS"],
            color=colors["BROWN"],
            style=self.BOLD + self.REVERSE,
            end_line=self.CONTINUE
        )

        self.text = StyleItems(
            symbol=symbols["LIST_ITEM"],
            color=colors["ORANGE"],
            style=self.NONE,
            end_line=self.CONTINUE
        )
