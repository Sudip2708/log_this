# print("cli_styler/_styles_settings/_prompt.py")
from ._base_calss import StyleBase, StyleItems


class PromptStyle(StyleBase):

    def __init__(self, colors, symbols):

        self.input = StyleItems(
            symbol=symbols["SELECTED"],
            color=colors["LAVENDER"],
            style=self.NONE,
            end_line=self.CONTINUE
        )

