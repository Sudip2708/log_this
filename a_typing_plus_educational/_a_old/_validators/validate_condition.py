class ValidateCondition:
    """
    Obecná validace podmínky s možností vyhození specifické výjimky.
    """

    def __call__(self, condition: bool) -> bool:
        """
        Validuje danou podmínku. Pokud podmínka není splněna, vyvolá výjimku nebo vrátí False.

        Args:
            condition: Výsledek podmínky (True/False).

        Returns:
            True pokud podmínka je True, jinak False nebo vyvolá výjimku.
        """
        if not condition:
            return False  # raise exception
        return True



