def is_named_tuple(annotation, bool_only=False):
    """Metoda pro ověření, že se jedná o NamedTuple objekt"""

    try:

        if (
                isinstance(annotation, type)
                and issubclass(annotation, tuple)
                and hasattr(annotation, "__annotations__")
                and hasattr(annotation, "_fields")
        ):
            return True

        # Pokud je žádost na bool odpověď
        if bool_only:
            return False

        # Dopsat výjimku když není NamedTuple
        raise NotNamedTupleError()

    # Dopsat zachytávání neplatných vstupů (když anotace není instance)
    except TypeError as e:
        raise MyTypeError()

    # Dopsat zachytávání neočekávaných výjimek
    except Exception as e:
        raise