from .data import (
    BaseStyle,
    StyleItems
)


class HintStyle(BaseStyle):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["INFO"],
            color=colors["PINK"],
            style=self.BOLD + self.REVERSE,
            end_line=self.END_LINE
        )

        self.text = StyleItems(
            symbol=symbols["LIST_ITEM"],
            color=colors["MAGENTA"],
            style=self.NONE,
            end_line=self.END_LINE
        )
