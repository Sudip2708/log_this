class GetIndentMethodMixins:

    def get_indent(self) -> str:
        """
        Vygeneruje odsazení podle aktuální hloubky volání.

        Metoda nejprve zjistí jaká je hodnota pro odsazení v konfiguračním souboru.
        Následně vrátí řetězec prázdných znaků, dle konfigurace a hloubky zanoření.

        Returns:
            str: Řetězec pro odsazení, nebo prázdný řetězec.
        """

        # Pokud je hodnota 0 a nebo není uvedená
        if not self.config["indent"]:
            return ""

        # ve všech ostatních případech
        return " " * self.config["indent"] * self.thread.current_depth