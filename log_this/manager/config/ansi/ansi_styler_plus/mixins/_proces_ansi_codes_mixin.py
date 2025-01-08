class ProcesAnsiCodesMixin:
    """Mixin pro metodu pro zpracování ansi kodů."""

    def proces_ansi_codes(self):
        """Metoda předspracuje získané ansi kody"""

        # Vytvoření proměné pro řetězce s ansi kody
        codes = []

        # Cyklus procházející obsah atributu pro ansi kody
        for style_name in self._styles:

            # Pokud je styl zapsán jako klíč povolených stylů
            if style_name in self._builder.config_dict:
                # Navrácení hodnoty pro daný klíč (ansi kod)
                # a přidání stylu do proměné pro ansi kody
                codes.append(self._builder.config_dict[style_name])

            # Pokud je styl zapsán jako ansi kod
            elif style_name in self._builder.allowed_codes:
                # Přidání stylu do proměné pro ansi kody
                codes.append(style_name)

        # Navrácení seznamu s ansi kody
        return codes