# print("cli_styler/_styles_settings/_menu.py")
from ._base_calss import StyleBase, StyleItems


class MenuStyle(StyleBase):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["DROPDOWN"],
            color=colors["DARK_GREEN"],
            style=self.BOLD + self.REVERSE,
            end_line=self.END_LINE
        )

        self.offer = StyleItems(
            symbol=symbols["UNSELECTED"],
            color=colors["LIGHT_GREEN"],
            style=self.NONE,
            end_line=self.END_LINE
        )

        self.selected = StyleItems(
            symbol=symbols["SELECTED"],
            color=colors["GREEN"],
            style=self.BOLD + self.REVERSE,
            end_line=self.END_LINE
        )
