import typing

def _union_typing(origin, args):
    # Zpracování Union typů

    from .parse_typing_annotation import parse_typing_annotation

    if origin is typing.Union:

        return {"union": tuple(parse_typing_annotation(arg) for arg in args)}