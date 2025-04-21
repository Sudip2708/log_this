import typing

def _literal_typing(origin, args):
    # Zpracování Literal

    if origin is typing.Literal:

        return {"literal": args}
