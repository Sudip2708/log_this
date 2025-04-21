class ConditionElseMixins:

    def _condition_else(self, words):
        """Zpracování 'else' větve podmínky."""
        # Kontrola, zda jsme v kontextu podmínky
        if self.current_context and self.current_context[-1][0] == "if":
            self.current_context.pop()  # Odstraníme 'if' z kontextu
            self.current_context.append(("else",))
            return {"condition": "else"}
        else:
            return {"error": "Else without if"}
