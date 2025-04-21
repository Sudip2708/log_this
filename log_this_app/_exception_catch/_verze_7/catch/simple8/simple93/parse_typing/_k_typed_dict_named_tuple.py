import typing
import inspect


def _typed_dict_named_tuple_typing(annotation):
    # Zpracování TypedDict, NamedTuple

    from .parse_typing_annotation import parse_typing_annotation

    if inspect.isclass(annotation) and hasattr(annotation, "__annotations__"):

        if (issubclass(annotation, typing.TypedDict)
                or issubclass(annotation, tuple)
                and hasattr(annotation, "_field_types")):

            field_types = {}

            if issubclass(annotation, typing.TypedDict):
                for field, field_type in annotation.__annotations__.items():
                    field_types[field] = parse_typing_annotation(field_type)
                return {"typed_dict": field_types}

            else:  # NamedTuple
                for field, field_type in annotation._field_types.items():
                    field_types[field] = parse_typing_annotation(field_type)
                return {"named_tuple": field_types}