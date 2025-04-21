

def _list_types(value, parsed_type):
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