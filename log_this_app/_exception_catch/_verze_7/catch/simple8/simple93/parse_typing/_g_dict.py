import typing

def _dict_typing(origin, args):
    # Zpracování Dict

    from .parse_typing_annotation import parse_typing_annotation

    if origin in (dict, typing.Dict):

        if len(args) == 0:
            return {"dict": ("Any", "Any")}

        elif len(args) == 2:
            return {"dict": (
            parse_typing_annotation(args[0]), parse_typing_annotation(args[1]))}
