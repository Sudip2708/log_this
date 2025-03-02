from .data import (
    BaseStyle,
    StyleItems
)


class InfoStyle(BaseStyle):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["INFO"],
            color=colors["LIGHT_PURPLE"],
            style=self.BOLD + self.REVERSE,
            end_line=self.NONE
        )

        self.text = StyleItems(
            symbol=symbols["LIST_ITEM"],
            color=colors["PURPLE"],
            style=self.NONE,
            end_line=self.NONE
        )

