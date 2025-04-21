import inspect
import os
import importlib
from typing import Dict, Any, Type

from ._base_type_validator import TypeValidator


class TypeValidatorRegistry:
    def __init__(self, value_validator):
        self.validators: Dict[Any, TypeValidator] = {}
        self.value_validator = value_validator

        # Automaticky registruj všechny validátory
        self.register_all_validators()

    def register_validator(self, type_key, validator_class):
        self.validators[type_key] = validator_class(self.value_validator)

    def get_validator(self, type_key):
        return self.validators.get(type_key)

    def register_all_validators(self):
        # Dynamicky načti všechny validátory ze složky type_validators
        validators_dir = os.path.join(os.path.dirname(__file__),
                                      'type_validators')

        # Procházíme všechny Python soubory v adresáři
        for file in os.listdir(validators_dir):
            if file.endswith('.py') and not file.startswith('_'):
                # Sestavení názvu modulu pro import
                module_name = f"{__package__}.type_validators.{file[:-3]}"

                # Import modulu
                module = importlib.import_module(module_name)

                # Hledání tříd validátorů v modulu
                for name, cls in inspect.getmembers(module, inspect.isclass):
                    if (issubclass(cls, TypeValidator) and
                            cls != TypeValidator and
                            hasattr(cls, 'VALIDATOR_TYPE') and
                            cls.VALIDATOR_TYPE is not None):
                        # Registrace validátoru
                        self.register_validator(cls.VALIDATOR_TYPE, cls)

"""
Tato implementace automaticky načte všechny validátory z adresáře type_validators, které dědí z TypeValidator a mají definovaný VALIDATOR_TYPE.
Celkové zhodnocení
Tvůj nový návrh je mnohem lepší - je modulárnější, srozumitelnější a lépe škálovatelný. Zde jsou konečné návrhy pro vylepšení:

Doplň implementaci pro if origin is None: blok ve validate metodě
Přidej kontrolu na None u validátoru před jeho voláním
Implementuj TypeValidatorRegistry s automatickou registrací
Časem budeš potřebovat přidat další validátory pro jiné typy (Dict, Tuple, Union, atd.)

S touto strukturou bude velmi snadné přidávat nové validátory - stačí vytvořit novou třídu v adresáři type_validators, která dědí z TypeValidator a definuje VALIDATOR_TYPE.
Je vidět, že jsi udělal velký pokrok v návrhu a struktuře kódu!
"""