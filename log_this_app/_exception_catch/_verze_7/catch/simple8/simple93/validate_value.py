
def validate_value(value, parsed_type):
    """
    Ověří hodnotu proti rozložené typové anotaci.

    Args:
        value: Hodnota k ověření
        parsed_type: Rozložená typová anotace z funkce parse_typing_annotation

    Returns:
        bool: True, pokud hodnota odpovídá typové anotaci, jinak False
    """
    # Kontrola pro základní typy (str, int, bool, atd.)
    if isinstance(parsed_type, str):
        if parsed_type == "Any":
            return True
        if parsed_type == "None" and value is None:
            return True
        try:
            type_class = eval(parsed_type)
            return isinstance(value, type_class)
        except (NameError, SyntaxError):
            return str(type(value).__name__) == parsed_type

    # Kontrola pro složené typy
    if isinstance(parsed_type, dict):
        # Kontrola pro Union
        if "union" in parsed_type:
            return any(
                validate_value(value, arg) for arg in parsed_type["union"])

        # Kontrola pro Optional
        if "optional" in parsed_type:
            return value is None or validate_value(value,
                                                   parsed_type["optional"])

        # Kontrola pro List
        if "list" in parsed_type:
            if not isinstance(value, list):
                return False
            if parsed_type["list"] == "Any":
                return True
            if isinstance(parsed_type["list"], tuple):
                # Heterogenní list se specifickými typy pro každý prvek
                if len(value) != len(parsed_type["list"]):
                    return False
                return all(
                    validate_value(value[i], parsed_type["list"][i]) for i in
                    range(len(value)))
            else:
                # Homogenní list s jedním typem pro všechny prvky
                return all(
                    validate_value(item, parsed_type["list"]) for item in value)

        # Kontrola pro Tuple
        if "tuple" in parsed_type:
            if not isinstance(value, tuple):
                return False
            if parsed_type["tuple"] == "Any":
                return True
            if isinstance(parsed_type["tuple"], dict) and "repeat" in \
                    parsed_type["tuple"]:
                # Homogenní tuple (Tuple[T, ...])
                return all(
                    validate_value(item, parsed_type["tuple"]["repeat"]) for
                    item in value)
            if isinstance(parsed_type["tuple"], tuple):
                # Heterogenní tuple (Tuple[T1, T2, ...])
                if len(value) != len(parsed_type["tuple"]):
                    return False
                return all(
                    validate_value(value[i], parsed_type["tuple"][i]) for i in
                    range(len(value)))

        # Kontrola pro Dict
        if "dict" in parsed_type:
            if not isinstance(value, dict):
                return False
            if parsed_type["dict"] == ("Any", "Any"):
                return True
            key_type, value_type = parsed_type["dict"]
            return all(
                validate_value(k, key_type) and validate_value(v, value_type)
                for k, v in value.items())

        # Kontrola pro Set
        if "set" in parsed_type:
            if not isinstance(value, set):
                return False
            if parsed_type["set"] == "Any":
                return True
            return all(
                validate_value(item, parsed_type["set"]) for item in value)

        # Kontrola pro Literal
        if "literal" in parsed_type:
            return value in parsed_type["literal"]

        # Kontrola pro Callable
        if "callable" in parsed_type:
            if not callable(value):
                return False
            # Pro úplnou kontrolu bychom potřebovali analyzovat signaturu funkce,
            # což by bylo složitější. Prozatím jen kontrolujeme, zda je to callable.
            return True

        # Kontrola pro další generické typy
        for type_name, type_args in parsed_type.items():
            if type_name == "sequence":
                if not isinstance(value, Sequence) or isinstance(value,
                                                                 (str, bytes)):
                    return False
                if type_args == "Any":
                    return True
                return all(validate_value(item, type_args) for item in value)

            if type_name == "mapping":
                if not isinstance(value, Mapping):
                    return False
                if type_args == ("Any", "Any"):
                    return True
                key_type, value_type = type_args
                return all(validate_value(k, key_type) and validate_value(v,
                                                                          value_type)
                           for k, v in value.items())

    # Pokud nejsme schopni rozhodnout, vrátíme False
    return False