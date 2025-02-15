from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit import print_formatted_text
from prompt_toolkit.styles import Style

# Import barev z cli_colors.py
from cli_color_claude2 import *


def create_color_preview():
    # Vytvoření slovníku stylů pro všechny barvy
    styles_dict = {
        # Červené odstíny
        "red.light": f"fg:{RED_LIGHT} bold",
        "red.dark": f"fg:{RED_DARK}",

        # Červeno-oranžové odstíny
        "red_orange.light": f"fg:{RED_ORANGE_LIGHT} bold",
        "red_orange.dark": f"fg:{RED_ORANGE_DARK}",

        # Oranžové odstíny
        "orange.light": f"fg:{ORANGE_LIGHT} bold",
        "orange.dark": f"fg:{ORANGE_DARK}",

        # Oranžovo-žluté odstíny
        "orange_yellow.light": f"fg:{ORANGE_YELLOW_LIGHT} bold",
        "orange_yellow.dark": f"fg:{ORANGE_YELLOW_DARK}",

        # Žluté odstíny
        "yellow.light": f"fg:{YELLOW_LIGHT} bold",
        "yellow.dark": f"fg:{YELLOW_DARK}",

        # Žluto-zelené odstíny
        "yellow_green.light": f"fg:{YELLOW_GREEN_LIGHT} bold",
        "yellow_green.dark": f"fg:{YELLOW_GREEN_DARK}",

        # Zelené odstíny
        "green.light": f"fg:{GREEN_LIGHT} bold",
        "green.dark": f"fg:{GREEN_DARK}",

        # Zeleno-modré odstíny
        "green_blue.light": f"fg:{GREEN_BLUE_LIGHT} bold",
        "green_blue.dark": f"fg:{GREEN_BLUE_DARK}",

        # Modré odstíny
        "blue.light": f"fg:{BLUE_LIGHT} bold",
        "blue.dark": f"fg:{BLUE_DARK}",

        # Modro-fialové odstíny
        "blue_violet.light": f"fg:{BLUE_VIOLET_LIGHT} bold",
        "blue_violet.dark": f"fg:{BLUE_VIOLET_DARK}",

        # Fialové odstíny
        "violet.light": f"fg:{VIOLET_LIGHT} bold",
        "violet.dark": f"fg:{VIOLET_DARK}",
    }

    style = Style.from_dict(styles_dict)

    # Vytvoření názvů pro zobrazení
    color_pairs = [
        ("RED", "red"),
        ("RED/ORANGE", "red_orange"),
        ("ORANGE", "orange"),
        ("ORANGE/YELLOW", "orange_yellow"),
        ("YELLOW", "yellow"),
        ("YELLOW/GREEN", "yellow_green"),
        ("GREEN", "green"),
        ("GREEN/BLUE", "green_blue"),
        ("BLUE", "blue"),
        ("BLUE/VIOLET", "blue_violet"),
        ("VIOLET", "violet")
    ]

    print("\nPřehled barev pro terminál:")
    print("=" * 40)

    for display_name, color_key in color_pairs:
        # Vytvoření formátovaného textu pro světlou barvu
        light_text = FormattedText([
            (f"class:{color_key}.light", f"{display_name}_LIGHT")
        ])

        # Vytvoření formátovaného textu pro tmavou barvu
        dark_text = FormattedText([
            (f"class:{color_key}.dark", f"{display_name.lower()}_dark")
        ])

        # Vytisknutí barev
        print_formatted_text(light_text, style=style)
        print_formatted_text(dark_text, style=style)
        print()  # Prázdný řádek pro lepší čitelnost


if __name__ == "__main__":
    create_color_preview()