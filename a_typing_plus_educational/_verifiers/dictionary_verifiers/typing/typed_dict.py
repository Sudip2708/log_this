from typing import TypedDict

from ...._bases import DictionaryValidatorBase
from ...._validators import dictionary_validator_for_typeddict


class TypedDictValidator(DictionaryValidatorBase):
    """
    Validátor pro typovou anotaci TypedDict

    TypedDict reprezentuje slovník se specifickými klíči a odpovídajícími typy hodnot.
    Na rozdíl od běžného Dict, TypedDict definuje konkrétní strukturu slovníku, kde
    každý klíč má předem určený název a typ své hodnoty. Funguje jako staticky typovaná
    varianta slovníku pro zkvalitnění typové kontroly.

    Syntaxe:
        - Deklarace pomocí třídy:
          class Config(TypedDict):
              host: str
              port: int
              debug: bool

        - Deklarace pomocí funkčního zápisu:
          Config = TypedDict('Config', {'host': str, 'port': int, 'debug': bool})

        - Nepovinné klíče (od Python 3.8) pomocí NotRequired:
          class Config(TypedDict):
              host: str
              port: NotRequired[int]  # port není povinný

        - Celková totalita (od Python 3.8):
          class Config(TypedDict, total=False):  # žádný klíč není povinný
              host: str
              port: int

    Příklady použití:
        - class Movie(TypedDict):
              title: str
              year: int
              director: str

        - class Person(TypedDict, total=False):
              name: str
              age: int  # nepovinný klíč

        - # Použití jako typová anotace
          def process_movie(movie: Movie) -> None: ...

        - # Vytvoření instance
          movie: Movie = {"title": "Metropolis", "year": 1927, "director": "Fritz Lang"}

    Validační proces:
        1. Ověří, zda hodnota je instance typu dict
        2. Zjistí, zda je TypedDict definován jako "total" (výchozí) nebo "non-total"
        3. Pro "total" TypedDict ověří:
           - zda slovník obsahuje přesně požadované klíče (ne více, ne méně)
           - zda všechny hodnoty odpovídají očekávaným typům
        4. Pro "non-total" TypedDict ověří:
           - zda slovník obsahuje všechny povinné klíče
           - zda všechny hodnoty, které jsou ve slovníku, odpovídají očekávaným typům
        5. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_config(config: AppConfig) -> None
        - Pro návratové hodnoty: def get_user_info() -> UserInfo
        - Pro typování proměnných: settings: ServerConfig = {"host": "localhost", "port": 8080}

    Kompatibilita:
        - TypedDict je na runtime úrovni běžným slovníkem (dict)
        - TypedDict je primárně nástrojem pro statickou analýzu kódu (mypy, pyright)
        - TypedDict není kompatibilní s Dict[str, Any] na úrovni statické typové kontroly
        - TypedDict nelze použít přímo s generickými typy

    Související typy:
        - Dict: obecný slovník s uniformním typem klíčů a hodnot
        - NamedTuple: podobný koncept pro tuple místo dict
        - dataclasses: plnohodnotnější alternativa pro definování datových struktur

    Omezení:
        - Klíče v TypedDict musí být vždy řetězce (str)
        - TypedDict neprovádí žádnou runtime validaci (ta je zajištěna až touto knihovnou)
        - Nelze dynamicky přidávat nové klíče do TypedDict definice
        - TypedDict nemá žádné speciální metody jako dataclasses

    Běžné chyby:
        - Záměna TypedDict za Dict[str, Union[...]]
        - Nesprávné očekávání runtime validace od samotného TypedDict
        - Pokus o použití jiných typů než str jako klíčů
        - Nedůsledné dodržování struktury TypedDict při vytváření instancí

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.TypedDict
        - https://peps.python.org/pep-0589/ (TypedDict)
        - https://peps.python.org/pep-0655/ (NotRequired a Required)
    """

    VALIDATOR_KEY = "typeddict"
    ANNOTATION = TypedDict
    INFO = "Definuje strukturovaný slovník, kde každý klíč má pevně daný typ hodnoty."
    ORIGIN = dict  # runtime je TypedDict instancí dict

    def __call__(self, value, annotation, depth_check, custom_types, bool_only):
        """Přetížení metody __call__ pro validaci slovníkových struktur."""

        # Navrácení výstupu funkce pro validaci slovníkových objektů upravené pro TypedDict
        return dictionary_validator_for_typeddict(
            value, self.ORIGIN, annotation, depth_check, custom_types, bool_only
        )