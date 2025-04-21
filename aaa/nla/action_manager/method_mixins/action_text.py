class ActionTextMixins:

    def _action_text(self, words):
        """Zpracování akce 'text'."""
        # Slova po 'text' reprezentují textový řetězec
        text = " ".join(words[1:])
        return {"text": text}