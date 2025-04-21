

def _tuple_types(value, parsed_type):
    # Kontrola pro Tuple

    if "tuple" in parsed_type:

        if not isinstance(value, tuple):
            return False

        if parsed_type["tuple"] == "Any":
            return True

        if isinstance(parsed_type["tuple"], dict) and "repeat" in parsed_type["tuple"]:

            # Homogenní tuple (Tuple[T, ...])
            return all(
                validate_value(item, parsed_type["tuple"]["repeat"])
                for item in value
            )

        if isinstance(parsed_type["tuple"], tuple):
            # Heterogenní tuple (Tuple[T1, T2, ...])

            if len(value) != len(parsed_type["tuple"]):
                return False
            return all(
                validate_value(value[i], parsed_type["tuple"][i])
                for i in range(len(value))
            )