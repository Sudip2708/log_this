import typing

def _tuple_typing(origin, args):
    # Zpracování Tuple

    from .parse_typing_annotation import parse_typing_annotation

    if origin in (tuple, typing.Tuple):

        if len(args) == 0:
            return {"tuple": "Any"}

        elif len(args) == 2 and args[1] is Ellipsis:
            # Tuple[T, ...] - homogenní tuple
            return {"tuple": {"repeat": parse_typing_annotation(args[0])}}

        else:
            # Tuple[T1, T2, ...] - heterogenní tuple
            return {
                "tuple": tuple(parse_typing_annotation(arg) for arg in args)}
