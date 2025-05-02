from inspect import signature

def function_signature_check(concat_args, value, bool_only):
    # První argument by měl být ParamSpec, následují typy argumentů
    # Ověření počtu parametrů funkce
    try:
        sig = signature(value)
        params = list(sig.parameters.values())

        # Počet explicitních parametrů v Concatenate (bez ParamSpec)
        explicit_params_count = len(concat_args) - 1

        # Velmi zjednodušená kontrola: funkce by měla mít alespoň tolik parametrů
        # kolik je specifikováno v Concatenate (bez ParamSpec)
        if len(params) < explicit_params_count:
            if bool_only:
                return False
            raise VerifyError(
                f"Funkce nemá dostatek parametrů pro Concatenate specifikaci. "
                f"Očekáváno alespoň {explicit_params_count}, ale má {len(params)}"
            )

        return True

    except ValueError:
        # Některé callable objekty nemají signaturu, kterou lze introspekovat
        if bool_only:
            return False
        raise VerifyError(
            f"Nelze analyzovat signaturu funkce pro validaci Concatenate: {value}"
        )