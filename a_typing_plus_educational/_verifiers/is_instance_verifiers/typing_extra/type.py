from typing import Type, get_args

from ..._bases import IsInstanceValidatorBase, T

from ...._exceptions import (
    VerifyTypeTypeError,
    VerifyInternalUnexpectedError,
    VerifyError,
)


class TypeValidator(IsInstanceValidatorBase):
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
    INFO = "Definuje typ na základě uvedené specifikace"
    ORIGIN = type

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):

        try:

            # Validace sebe sama (origin)
            self.validate_native_type(value, self.GET_ORIGIN)

            # Kontrola zda je požadavek i na vnitřní validaci
            if not depth_check:
                return True

            # Načtení vnitřních anotací
            inner_args = get_args(annotation)

            # Pokud není specifikován konkrétní typ, vrátíme True
            if inner_args is None or inner_args == Ellipsis:
                return True

            # Kontrola, zda je třída podtřídou specifikované třídy
            if issubclass(value, inner_args):
                return True

            # Kontrola zda odpověď má být bool
            if bool_only:
                return False

            # Vyvolání výjimky s oznamem o nevalidní hodnotě
            raise VerifyTypeTypeError(value, inner_args)

        # Propagace vyvolané výjimky
        except VerifyError:
            raise

        # Zachycení neočekávaných výjimek
        except Exception as e:
            raise VerifyInternalUnexpectedError(
                info="Nastala chyba při ověřování objektu.",
                modul="Zachyceno v třídě TypeValidator",
                original_exception=e
            ) from e