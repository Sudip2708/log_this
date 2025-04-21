import typing

def _callable_typing(origin, args):
    # Zpracování Callable

    from .parse_typing_annotation import parse_typing_annotation

    if origin is typing.Callable:

        if len(args) == 0 or args[0] is Ellipsis:
            return {
                "callable": (
                    "Any", parse_typing_annotation(args[1])
                    if len(args) > 1
                    else "Any"
                )
            }

        else:
            params = [parse_typing_annotation(arg) for arg in args[0]]
            return_type = parse_typing_annotation(args[1]) if len(args) > 1 else "Any"
            return {"callable": (params, return_type)}
