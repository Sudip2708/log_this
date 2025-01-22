

class ShowHelpMixin:

    @staticmethod
    def _show_help() -> None:
        """Zobrazí nápovědu pro používání interaktivního režimu."""
        help_text = """
        Nápověda pro interaktivní režim:

        1. Navigace
           - Použijte šipky nahoru/dolů pro pohyb v menu
           - Potvrďte výběr klávesou Enter
           - Escape nebo Ctrl+C pro návrat/zrušení

        2. Změna konfigurace
           - Vyberte klíč, který chcete změnit
           - Zadejte novou hodnotu podle zobrazené nápovědy
           - Hodnota bude validována před uložením

        3. Tipy
           - U každého klíče je zobrazena aktuální a výchozí hodnota
           - Nápověda obsahuje povolené hodnoty a jejich význam
        """

        print(help_text)
        input("\nStiskněte Enter pro návrat do hlavního menu...")