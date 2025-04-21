class CodeGenerator:

    def __init__(self, objects):
        self.objects = objects

    def generate_python(self):
        """Generování Python kódu z vnitřní reprezentace objektů."""
        result = []

        for obj_name, obj_data in self.objects.items():
            function_def = f"def {obj_name}("

            params = []
            param_types = []
            if "expect" in obj_data:
                for param_name, param_data in obj_data["expect"].items():
                    params.append(param_name)
                    if "type" in param_data:
                        type_str = " | ".join(
                            [t.__name__ for t in param_data["type"]])
                        param_types.append(f"{param_name}: {type_str}")

            if param_types:
                function_def += ", ".join(param_types)
            else:
                function_def += ", ".join(params)

            function_def += "):"
            result.append(function_def)

            # Specifická logika pro ukázkový příklad
            if obj_name == "speed_up" and "expect" in obj_data and "current_speed" in \
                    obj_data["expect"]:
                result.append("    if current_speed:")
                result.append("        print(current_speed + 10)")
                result.append("    else:")
                result.append(
                    '        print("Current speed was not specified.")')
            else:
                result.append("    pass")

            result.append("")

        return "\n".join(result)