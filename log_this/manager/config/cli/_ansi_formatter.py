class ANSIFormatter:
    """
    Třída pro generování ANSI sekvencí pro formátování textu.
    """
    # Mapování stylů a barev na ANSI kódy
    STYLES = {
        "reset": "0",
        "bold": "1",
        "dim": "2",
        "italic": "3",
        "underline": "4",
        "inverse": "7",
        "strikethrough": "9",
    }

    COLORS = {
        "black": "30",
        "red": "31",
        "green": "32",
        "yellow": "33",
        "blue": "34",
        "magenta": "35",
        "cyan": "36",
        "white": "37",
        "bright_black": "90",
        "bright_red": "91",
        "bright_green": "92",
        "bright_yellow": "93",
        "bright_blue": "94",
        "bright_magenta": "95",
        "bright_cyan": "96",
        "bright_white": "97",
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
        "bright_bg_black": "100",
        "bright_bg_red": "101",
        "bright_bg_green": "102",
        "bright_bg_yellow": "103",
        "bright_bg_blue": "104",
        "bright_bg_magenta": "105",
        "bright_bg_cyan": "106",
        "bright_bg_white": "107",
    }

    @classmethod
    def style_set(cls, *args):
        """
        Generuje ANSI sekvenci na základě zadaných stylů a barev.

        Args:
            *args (str): Seznam stylů nebo barev jako klíčová slova (např. "bold", "red").

        Returns:
            str: ANSI kód formátování.
        """
        codes = []
        for arg in args:
            if arg in cls.STYLES:
                codes.append(cls.STYLES[arg])
            elif arg in cls.COLORS:
                codes.append(cls.COLORS[arg])
            elif arg in cls.BACKGROUND_COLORS:
                codes.append(cls.BACKGROUND_COLORS[arg])
            else:
                raise ValueError(f"Neznámý styl nebo barva: {arg}")
        return f"\033[{';'.join(codes)}m"

    @staticmethod
    def style_reset():
        """
        Vrací sekvenci pro resetování stylu.

        Returns:
            str: ANSI kód resetování stylu.
        """
        return "\033[0m"

# Příklad použití
if __name__ == "__main__":
    formatter = ANSIFormatter()

    # Použití metody style_set a style_reset
    print(f"{formatter.style_set('bold', 'red')}Toto je tučný červený text.{formatter.style_reset()}")
    print(f"{formatter.style_set('underline', 'blue')}Podtržený modrý text.{formatter.style_reset()}")
    print(f"{formatter.style_set('bright_green', 'bg_black')}Světle zelený text s černým pozadím.{formatter.style_reset()}")
