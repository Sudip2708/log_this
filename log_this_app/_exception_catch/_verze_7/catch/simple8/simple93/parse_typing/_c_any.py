import typing

def _any_typing(annotation):
    # Zpracování Any

    if annotation is typing.Any:

        return "Any"