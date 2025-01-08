# file: _ansi_codes.py
TEXT_STYLES = {
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

# LEVELS_COLORS = {
#     'ERROR': "31",  # red
#     'WARNING': "33",  # yellow
#     'INFO': "32",  # green
#     'DEBUG': "36",  # cyan
#     'CRITICAL': '36;43',  # red with yellow background
# }
#
# LEVELS_COLORS_SMALL = {
#     'error': "31",  # red
#     'warning': "33",  # yellow
#     'info': "32",  # green
#     'debug': "36",  # cyan
#     'critical': '36;43',  # red with yellow background
# }