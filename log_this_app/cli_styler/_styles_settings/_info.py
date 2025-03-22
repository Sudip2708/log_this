# print("cli_styler/_styles_settings/_info.py")
from ._base_calss import StyleBase, StyleItems


class InfoStyle(StyleBase):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["INFO"],
            color=colors["LIGHT_PURPLE"],
            style=self.BOLD + self.REVERSE,
            end_line=self.CONTINUE
        )

        self.text = StyleItems(
            symbol=symbols["LIST_ITEM"],
            color=colors["PURPLE"],
            style=self.NONE,
            end_line=self.CONTINUE
        )

        self.text_blank = StyleItems(
            symbol=symbols["UNSELECTED"],
            color=colors["PURPLE"],
            style=self.NONE,
            end_line=self.CONTINUE
        )

