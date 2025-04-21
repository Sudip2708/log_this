class ObjectUseMixins:

    def _object_use(self, words):
        """Zpracování akce 'object' a nalezení existujícího objektu."""
        # Slova po 'object' až do dalšího klíčového slova reprezentují název objektu
        object_name_words = []
        i = 1  # Přeskočíme slovo 'object'

        while i < len(words):
            if words[i] in self.actions:
                break
            object_name_words.append(words[i])
            i += 1

        object_name = "_".join(object_name_words)

        # Kontrola, zda objekt existuje
        if object_name in self.objects:
            self.current_object = object_name
            self.current_context = []
            return {"using_object": object_name}
        else:
            return {"error": f"Object {object_name} not found"}

