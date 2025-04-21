# validators/collections/defaultdict_validator.py

from typing import Any, DefaultDict
from collections import defaultdict

from ._dict_alike_base import DictAlikeBase

K = V = Any

class DefaultDictValidator(DictAlikeBase):
    """
    Validátor pro zápis collections.defaultdict[K, V]

    Přebírá logiku validace slovníku – validuje klíče a hodnoty.

    DefaultDict je slovník, který automaticky vytváří výchozí hodnotu
    pro neexistující klíče pomocí zadané tovární funkce.
    Je užitečný pro práci se skupinováním nebo počítáním.

    Hint:
        defaultdict[K, V] = Slovník s výchozí hodnotou a klíči typu K a hodnotami typu V
    """

    VALIDATOR_KEY = "defaultdict"
    ANNOTATION = DefaultDict[K,V]
    INFO = "Definuje slovník typu defaultdict s typovanými klíči a hodnotami."
    GET_ORIGIN = defaultdict  # collections.defaultdict
