import typing

def _sequence_mapping_typing(origin, args):
    # Zpracování dalších generických typů (Sequence, Mapping, atd.)

    from .parse_typing_annotation import parse_typing_annotation


    if origin is not None:

        origin_name = getattr(origin, "__name__", str(origin))

        if len(args) == 0:
            return {origin_name.lower(): "Any"}

        elif len(args) == 1:
            return {origin_name.lower(): parse_typing_annotation(args[0])}

        else:
            return {origin_name.lower(): tuple(
                parse_typing_annotation(arg) for arg in args)}