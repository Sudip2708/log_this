from collections import UserList

from .._base_iterable_validator import BaseIterableValidator
from .._base_type_variables import T


class UserListValidator(BaseIterableValidator):
    """
    Validátor pro zápis UserList[T]

    Hint:
        UserList[T] = Speciální list určený k dědění a přizpůsobení chování
    """

    VALIDATOR_KEY = "userlist"
    ANNOTATION = UserList[T]
    INFO = "Definuje přizpůsobitelný seznam založený na UserList"
    GET_ORIGIN = UserList
