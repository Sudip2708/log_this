from .data import (
    BaseStyle,
    StyleItems
)


class WarningStyle(BaseStyle):

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

