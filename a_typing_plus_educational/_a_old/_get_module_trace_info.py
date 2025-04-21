import traceback

def get_module_trace_info():
    stack = traceback.extract_stack()
    # -2 je aktuální funkce, -3 je volající
    if len(stack) > 2:
        filename, lineno, func, text = stack[-3]
        return f"{filename}:{lineno} → {func}()"
    return "Neznámý kontext"

