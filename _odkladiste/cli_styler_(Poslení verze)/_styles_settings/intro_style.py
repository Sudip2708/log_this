from .data import (
    BaseStyle,
    StyleItems
)


class IntroStyle(BaseStyle):

    def __init__(self, colors, symbols):

        self.title = StyleItems(
            symbol=symbols["INTRO"],
            color=colors["BLUE"],
            style=self.BOLD + self.REVERSE,
            end_line=self.END_LINE
        )

        self.end = StyleItems(
            symbol=self.NONE,
            color=colors["BLUE"],
            style=self.NONE,
            end_line=self.END_LINE
        )


