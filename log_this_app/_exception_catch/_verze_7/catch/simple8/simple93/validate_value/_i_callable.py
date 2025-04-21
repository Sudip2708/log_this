

def _callable_types(value, parsed_type):
    # Kontrola pro Callable

    if "callable" in parsed_type:

        if not callable(value):
            return False

        # Pro úplnou kontrolu bychom potřebovali analyzovat signaturu funkce,
        # což by bylo složitější. Prozatím jen kontrolujeme, zda je to callable.
        return True