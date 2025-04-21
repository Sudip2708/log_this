

def _base_typing(annotation, origin):
    # Zpracování základních typů (str, int, bool, atd.)

    if origin is None and isinstance(annotation, type):

        return annotation.__name__