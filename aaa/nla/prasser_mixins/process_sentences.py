class ProcessSentencesMixins:

    def process_sentences(self, sentences):
        """Zpracování jednotlivých vět."""
        results = []

        for sentence in sentences:
            # Rozdělení věty na souvětí
            clauses = self.split_into_clauses(sentence)

            # Zpracování každého souvětí
            processed_clauses = []
            for clause in clauses:
                words = self.split_into_words(clause)
                processed = self.process_words(words)
                processed_clauses.append(processed)

            results.append({
                "sentence": sentence,
                "clauses": clauses,
                "processed": processed_clauses
            })

        return results