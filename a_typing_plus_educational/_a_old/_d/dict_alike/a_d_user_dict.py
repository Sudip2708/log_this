from typing import Any
from collections import UserDict

from ._dict_alike_base import DictAlikeBase

K = V = Any


class UserDictValidator(DictAlikeBase):
    """
    Validátor pro zápis collections.UserDict

    Přebírá logiku validace slovníku – validuje klíče a hodnoty.

    UserDict je základní třída pro vlastní implementace slovníků.
    Interně ukládá data v atributu .data, který je standardní dict.

    Hint:
        UserDict = Základní třída pro vytváření vlastních typů slovníků
    """

    VALIDATOR_KEY = "userdict"
    ANNOTATION = UserDict
    INFO = "Definuje vlastní implementaci slovníku pomocí UserDict."
    GET_ORIGIN = UserDict  # collections.UserDict

