from ._serialize_dataclass import serialize_dataclass
from ._serialize_dict import serialize_dict
from ._serialize_iterable import serialize_iterable
from ._serialize_namedtuple import serialize_namedtuple
from ._serialize_object_with_dict import serialize_object_with_dict

__all__ = [
    "serialize_dataclass",  # Serializuje dataclass objekty.
    "serialize_dict",  # Serializuje slovníky.
    "serialize_iterable",  # Serializuje iterovatelné struktury (list, tuple, set).
    "serialize_namedtuple",  # Serializuje namedtuple objekty.
    "serialize_object_with_dict",  # Serializuje objekty s __dict__ atributem.
]