import typing

def _set_typing(origin, args):
    # Zpracování Set

    from .parse_typing_annotation import parse_typing_annotation

    if origin in (set, typing.Set):

        if len(args) == 0:
            return {"set": "Any"}

        elif len(args) == 1:
            return {"set": parse_typing_annotation(args[0])}
