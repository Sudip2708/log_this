from typing import get_type_hints


def get_type_hints_safe(annotation):

    try:
        return get_type_hints(annotation)

    except TypeError as e:
        print(f"Došlo k chybě: {e}")

    except NameError as e:
        print(f"Došlo k chybě: {e}")

    except Exception as e:
        print(f"Došlo k chybě: {e}")