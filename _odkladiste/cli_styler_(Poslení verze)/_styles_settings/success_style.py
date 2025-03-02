from .data import (
    BaseStyle,
    StyleItems
)


class SuccessStyle(BaseStyle):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["ERROR"],
            color=colors["LIGHT_RED"],
            style=self.BOLD + self.REVERSE,
            end_line=self.END_LINE
        )

        self.text = StyleItems(
            symbol=symbols["LIST"],
            color=colors["RED"],
            style=self.BOLD + self.REVERSE,
            end_line=self.CONTINUE
        )
