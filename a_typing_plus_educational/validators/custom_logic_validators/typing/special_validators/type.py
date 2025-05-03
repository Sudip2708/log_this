from typing import Type

from ....._bases import BaseCustomLogicValidator, T
from ....._verifiers import type_verifier


class TypeValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci Type[T]

    Type[T] reprezentuje třídu (typ) objektu, nikoli instanci. Používá se pro anotaci
    parametrů a proměnných, které by měly obsahovat třídu (jako typ), nikoli instanci třídy.
    Type[T] lze také parametrizovat k určení, že třída by měla být podtřídou konkrétní třídy.

    Syntaxe:
        - Type                # Jakákoliv třída
        - Type[BaseClass]     # Třída, která je podtřídou BaseClass
        - Type[T]             # Při použití s generickým typem, třída odvozená od T

    Příklady použití:
        - Type                         # Libovolná třída
        - Type[int]                    # Třída int (ne instance)
        - Type[List[str]]              # Třída List parametrizovaná str
        - Type[BaseModel]              # Třída, která je podtřídou BaseModel
        - Type[Protocol]               # Třída implementující daný protokol

    Validační proces:
        1. Nejprve ověří, zda hodnota je instance typu 'type' (je třídou)
        2. Pokud je vyžadována hloubková kontrola (depth_check=True):
           a. Získá vnitřní parametr T z anotace pomocí get_args
           b. Pokud není parametr specifikován, validace projde
           c. Ověří, zda je hodnota podtřídou specifikované třídy pomocí issubclass
        3. V případě neúspěchu buď vrátí False (bool_only=True) nebo vyvolá VerifyTypeTypeError

    Použití v kódu:
        - Pro parametry funkcí továrního typu:
          def create_instance(cls: Type[User]) -> User
        - Pro registry tříd:
          def register_model(model_class: Type[BaseModel]) -> None
        - Pro funkce pracující s metadaty tříd:
          def get_table_name(entity_class: Type[Entity]) -> str
        - Pro typy v dekorátorech:
          def register(cls: Type) -> Type

    Rozdíl mezi Type[T] a T:
        - Type[T] reprezentuje třídu, která je podtřídou T
        - T reprezentuje instanci třídy T
        - Příklad: Type[User] je třída User, zatímco User je instance třídy User

    Běžné scénáře použití:
        - Tovární funkce vytvářející instance
        - Metaprogramování a práce s třídami
        - Systémy závislostí a vstřikování závislostí
        - Registrace tříd v rámci frameworků
        - Reflexe a introspekce kódu

    Běžné chyby:
        - Záměna Type[T] za T (předání instance místo třídy)
        - Předání instance třídy (obj) místo třídy samotné (obj.__class__)
        - Nesprávné zacházení s generickými typy v kombinaci s Type
        - Ignorování Type u metaklas

    Poznámky k výjimkám:
        - VerifyTypeTypeError je vyvolána, když předaná třída není podtřídou požadované třídy
        - Obsahuje informace o očekávané třídě a aktuální hodnotě

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.Type
        - https://peps.python.org/pep-0484/#the-type-of-class-objects
        - https://mypy.readthedocs.io/en/stable/kinds_of_types.html#class-types
    """

    VALIDATOR_KEY = "type"
    ANNOTATION = Type[T]

    IS_INSTANCE = type
    DUCK_TYPING = None

    DESCRIPTION = "Typ objektu jako hodnota"
    LONG_DESCRIPTION = (
            "Validuje, že hodnota je instancí typu Type, což značí samotný typ "
            "jako hodnotu (např. Type[str] označuje třídu str)."
        )

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Definice metody __call__ pro ověření Type."""

        return type_verifier(
            value, self.ORIGIN, annotation, depth_check, bool_only
        )