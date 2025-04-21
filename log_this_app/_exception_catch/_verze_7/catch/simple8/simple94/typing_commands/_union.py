def _union(code, value, extras, inner_check):
    for item in value:
        if not recursive_validator(code, item, inner_check, extras):
            raise
    return True
