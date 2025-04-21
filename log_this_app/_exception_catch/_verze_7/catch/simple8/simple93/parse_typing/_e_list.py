import typing

def _list_typing(origin, args):
    # Zpracování List

    from .parse_typing_annotation import parse_typing_annotation


    if origin in (list, typing.List):

        if len(args) == 0:
            return {"list": "Any"}

        elif len(args) == 1:
            return {"list": parse_typing_annotation(args[0])}

        else:
            return {"list": tuple(parse_typing_annotation(arg) for arg in args)}
