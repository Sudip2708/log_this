print("_ansi_codes.py")
# file: _ansi_codes.py
TEXT_STYLES = {
    "reset": "0",
    "bold": "1",
    "dim": "2",
    "italic": "3",
    "underline": "4",
    "blink": "5",
    "reverse": "7",
    "hidden": "8",
    "strike": "9",
    "double_underline": "21",
    "framed": "53",
}

TEXT_COLORS = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
    "default": "39",
    "gray": "90",
}

BACKGROUND_COLORS = {
    "bg_black": "40",
    "bg_red": "41",
    "bg_green": "42",
    "bg_yellow": "43",
    "bg_blue": "44",
    "bg_magenta": "45",
    "bg_cyan": "46",
    "bg_white": "47",
    "bg_default": "49",
}

LEVELS_COLORS = {
    'ERROR': "31;1",  # bold red
    'CRITICAL': "37;41",  # white text on red background
    'WARNING': "33;1",  # bold yellow
    'INFO': "32",  # green (normal)
    'DEBUG': "36",  # cyan (normal)
    'SUCCESS': "32;1",  # bold green
    'CONFIG': "34;1"  # bold blue
}

MESSAGE_COLORS = {
    'ERROR': "0",  # default color (reset)
    'CRITICAL': "37;41",  # white text on red background
    'WARNING': "0",  # default color (reset)
    'INFO': "0",  # default color (reset)
    'DEBUG': "90",  # gray
    'SUCCESS': "0",  # default color (reset)
    'CONFIG': "0"  # default color (reset)
}