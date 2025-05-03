from typing import Self

from ...._bases import BaseIsInstanceValidator
from ...._verifiers import is_instance_verifier_for_self


class SelfValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci typing.Self

    Typ Self umožňuje přesně označit návratový typ metody jako aktuální typ třídy,
    ve které je metoda definována. Je užitečný pro metody, které vracejí instanci
    stejné třídy, zejména pro metody řetězení a pro metody továrních tříd.

    Syntaxe:
        - Self               # Vyžaduje import z modulu typing (from typing import Self)
        - typing.Self        # Alternativní zápis (import typing)

    Příklady použití:
        - def set_name(self, name: str) -> Self: ...
        - @classmethod
          def from_config(cls, config: dict) -> Self: ...
        - def clone(self) -> Self: ...

    Implementační detaily:
        Self je speciální typová anotace, která odkazuje na typ aktuální třídy. Není to běžný typ,
        ale spíše reference na typ třídy, ve které je použita. Během typové kontroly se Self
        vyhodnotí jako aktuální třída, ale v runtime je to jen placeholder.

    Validační proces:
        1. Self je typová anotace používaná hlavně pro statickou kontrolu typů
        2. Validace v runtime by vyžadovala znalost aktuální třídy, ze které se validation volá
        3. Pro jednoduchost validátor ověří, zda je hodnota instance stejné třídy jako self

    Použití v kódu:
        - Pro návratové hodnoty metod řetězení: def add(self, x: int) -> Self: ...
        - Pro tovární metody: @classmethod def create(cls, data: dict) -> Self: ...
        - Pro metody klonování: def copy(self) -> Self: ...

    Srovnání s podobnými typy:
        - TypeVar s bound parametrem: Starší způsob řešení tohoto problému, méně přesný
        - Type[Self]: Používá se pro anotaci třídy místo instance

    Běžné vzory použití:
        - Metody řetězení:
          ```
          class Builder:
              def add_item(self, item: str) -> Self:
                  self.items.append(item)
                  return self
          ```
        - Tovární metody:
          ```
          class User:
              @classmethod
              def from_dict(cls, data: dict) -> Self:
                  return cls(data['name'], data['email'])
          ```
        - Metody klonování a kopírování:
          ```
          def copy(self) -> Self:
              return type(self)(**self.__dict__)
          ```

    Běžné chyby:
        - Použití Self mimo kontext třídy
        - Záměna s self parametrem (Self s velkým S je typová anotace)
        - Předpoklad, že Self automaticky zajistí správné typování dědičnosti

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Self
        - https://peps.python.org/pep-0673/ (Self Type)
    """

    VALIDATOR_KEY = "self"
    ANNOTATION = Self

    IS_INSTANCE = Self
    DUCK_TYPING = None

    DESCRIPTION = "Odkaz na typ aktuální třídy"
    LONG_DESCRIPTION = (
            "Validuje, že typ používá Self, "
            "což označuje typ aktuální třídy v rámci třídy samotné. "
            "Používá se v metodách, které vracejí instanci stejné třídy."
        )


    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření Literal."""

        return is_instance_verifier_for_self(value, self.ORIGIN, custom_types, bool_only)