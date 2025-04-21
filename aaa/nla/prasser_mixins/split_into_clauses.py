class SplitIntoClausesMixins:

    def split_into_clauses(self, sentence):
        """Rozdělení věty na souvětí dle čárky s mezerou za ní."""
        clauses = []
        current_clause = ""

        i = 0
        while i < len(sentence):
            if sentence[i:i + 2] == ", ":
                current_clause += sentence[i]
                clauses.append(current_clause.strip())
                current_clause = ""
                i += 2
            else:
                current_clause += sentence[i]
                i += 1

        # Přidání posledního souvětí, pokud existuje
        if current_clause.strip():
            clauses.append(current_clause.strip())

        return clauses