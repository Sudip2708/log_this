from collections import UserDict

from .._base_mapping_validator import BaseMappingValidator


class UserDictValidator(BaseMappingValidator):
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
    ORIGIN = UserDict

