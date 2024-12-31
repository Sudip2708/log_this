from ._dict_error_check import DictErrorCheckMixin
from ._serialize_dunder_dict import SerializeDunderDictMixin
from ._serialize_dunder_dataclass_fields import SerializeDunderDataclassFieldsMixin
from ._serialize_list_tuple_set import SerializeListTupleSetMixin
from ._serialize_dict import SerializeDictMixin


__all__ = [
    "DictErrorCheckMixin",  # Metoda pro kontrlolu a případnou úpravu slovníku, pokud obsahuje oznam o chybě.
    "SerializeDunderDictMixin",  # Serializuje objekty s __dict__ atributem.
    "SerializeDunderDataclassFieldsMixin",  # Serializuje dataclass objekty.
    "SerializeListTupleSetMixin",  # Serializuje seznamy, tuple a množiny.
    "SerializeDictMixin",  # Serializuje slovníky.
]