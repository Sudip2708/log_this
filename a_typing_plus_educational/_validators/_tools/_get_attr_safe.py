_MISSING = object()

def get_attr_safe(object, name, default=_MISSING):


    try:

        if default is _MISSING:
            return getattr(object, name)
        else:
            return getattr(object, name, default)

    except AttributeError as e:
        print(f"Oběkt nemá daný atribut: {e}")

    except Exception as e:
        print(f"Došlo k chybě: {e}")