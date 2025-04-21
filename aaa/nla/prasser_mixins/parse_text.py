class ParseTextMixins:

    def parse_text(self, text):
        """Zpracování celého textu a jeho rozdělení na věty."""
        sentences = []
        current_sentence = ""

        i = 0
        while i < len(text):
            if text[i:i + 2] == ". " or text[i:i + 2] == ".\n":
                current_sentence += text[i]
                sentences.append(current_sentence.strip())
                current_sentence = ""
                i += 2
            else:
                current_sentence += text[i]
                i += 1

        # Přidání poslední věty, pokud existuje
        if current_sentence.strip():
            sentences.append(current_sentence.strip())

        return self.process_sentences(sentences)