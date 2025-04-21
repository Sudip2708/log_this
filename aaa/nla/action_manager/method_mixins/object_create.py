class ObjectCreateMixins:

    def _object_create(self, words):
        """Zpracování akce 'create object'."""

        # Slova po 'create object' až do konce reprezentují název objektu
        object_name_words = words[2:]
        object_name = "_".join(object_name_words)

        # Vytvoření nového objektu
        self.objects[object_name] = {
            "name": tuple(object_name_words),
            "type": "object"
        }

        self.current_object = object_name
        return {"created_object": object_name}

