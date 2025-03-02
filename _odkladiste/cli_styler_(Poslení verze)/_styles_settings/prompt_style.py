from .data import (
    BaseStyle,
    StyleItems
)


class PromptStyle(BaseStyle):

    def __init__(self, colors, symbols):

        self.input = StyleItems(
            symbol=symbols["SELECTED"],
            color=colors["LAVENDER"],
            style=self.NONE,
            end_line=self.CONTINUE
        )

