from typing import Any
from collections import UserList

from ._list_alike_base import ListAlikeBase

T = Any

class UserListValidator(ListAlikeBase):
    """
    Validátor pro zápis UserList[T]

    Hint:
        UserList[T] = Speciální list určený k dědění a přizpůsobení chování
    """

    VALIDATOR_KEY = "userlist"
    ANNOTATION = UserList[T]
    INFO = "Definuje přizpůsobitelný seznam založený na UserList"
    GET_ORIGIN = UserList
