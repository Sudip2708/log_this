class SplitIntoWordsMixins:

    def split_into_words(self, clause):
        """Rozdělení souvětí na slova."""
        # Odstranění interpunkce na konci
        clause = clause.rstrip('.,:;!?')
        # Rozdělení podle mezer
        words = [word.lower() for word in clause.split()]
        return words