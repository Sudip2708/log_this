from dataclasses import dataclass
from prompt_toolkit import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText

@dataclass
class StyleItems:
    symbol: str
    color: str
    style: str
    end_line: str

    def __call__(self, text: str) -> tuple:
        return f"{self.color}{self.style}", f"{self.symbol}{text}{self.end_line}"