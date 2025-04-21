import typing

def _optional_typing(origin, args):
    # Zpracování Optional (což je vlastně Union[type, None])

    from .parse_typing_annotation import parse_typing_annotation


    if origin is typing.Union and type(None) in args:

        non_none_args = [arg for arg in args if arg is not type(None)]

        if len(non_none_args) == 1:
            return {"optional": parse_typing_annotation(non_none_args[0])}

        else:
            return {"optional": {"union": tuple(
                parse_typing_annotation(arg)
                for arg in non_none_args
            )}}