from collections import UserDict

from ..._bases import BaseMappingValidator, K, V


class UserDictValidator(BaseMappingValidator):
    """
    Validátor pro typovou anotaci UserDict[K, V]

    UserDict je základní třída pro vytváření vlastních implementací slovníků v Pythonu.
    Na rozdíl od přímého odvození od dict, UserDict poskytuje bezpečnější a flexibilnější
    způsob, jak rozšířit slovníkové chování. Interně ukládá data v atributu .data,
    který je standardním dict objektem.

    Syntaxe:
        - UserDict[K, V]              # Vyžaduje import z collections
        - collections.UserDict[K, V]  # Plně kvalifikovaný název
        - collections.UserDict        # Obecný UserDict bez specifikace typů

    Příklady použití:
        - UserDict[str, int]          # UserDict s řetězcovými klíči a celočíselnými hodnotami
        - UserDict[int, List[str]]    # UserDict s celočíselnými klíči a seznamy řetězců
        - UserDict[str, Any]          # UserDict s řetězcovými klíči a libovolnými hodnotami
        - UserDict[K, Dict[str, V]]   # UserDict s klíči typu K a hodnotami typu Dict[str, V]

    Vnitřní typy:
        Anotace UserDict vyžaduje specifikaci dvou typových parametrů:
        - K: Typ klíčů (musí být hashable)
        - V: Typ hodnot (libovolný podporovaný typ)

    Validační proces:
        1. Ověří, zda hodnota je instance typu collections.UserDict
        2. Pokud je požadována hloubková kontrola, ověří typy všech klíčů a hodnot
        3. Rekurzivně validuje vnořené typy dle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_config(config: UserDict[str, Any]) -> None
        - Pro návratové hodnoty: def create_counters() -> UserDict[str, int]
        - Pro typování proměnných: class MyDict(UserDict[str, int]): pass

    Srovnání s podobnými typy:
        - UserDict vs dict: UserDict je určený pro odvozování vlastních slovníkových tříd,
          zatímco přímé odvození od dict může být problematické kvůli C implementaci
        - UserDict vs MutableMapping: UserDict je konkrétní implementace MutableMapping
          určená pro snadné rozšíření
        - UserDict vs defaultdict/OrderedDict: UserDict je základní třída pro vlastní implementace,
          zatímco defaultdict a OrderedDict jsou speciální slovníky pro konkrétní účely

    Běžné vzory použití:
        - Vytváření vlastních slovníkových tříd: class LoggingDict(UserDict[K, V])
        - Rozšíření chování slovníku: class ValidatingDict(UserDict[str, int])
        - Kontrola typů při vkládání: class TypedDict(UserDict[K, V])
        - Přidání dodatečných metod ke slovníku: class EnhancedDict(UserDict[K, V])

    Běžné chyby:
        - Zapomenutí importu: from collections import UserDict
        - Přístup k uloženým datům mimo .data atribut
        - Záměna s TypedDict z modulu typing (která má jiný účel)
        - Nesprávná implementace __init__ bez volání super().__init__()

    Reference:
        - https://docs.python.org/3/library/collections.html#collections.UserDict
        - https://docs.python.org/3/library/typing.html#typing-generics
        - https://peps.python.org/pep-0585/ (nativní generické typy)
    """

    VALIDATOR_KEY = "userdict"
    ANNOTATION = UserDict[K, V]
    INFO = "Definuje vlastní implementaci slovníku pomocí UserDict."
    ORIGIN = UserDict