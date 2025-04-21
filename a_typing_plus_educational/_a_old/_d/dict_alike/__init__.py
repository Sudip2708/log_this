from .dict import DictValidator
from .mapping import MappingValidator
from .mutable_mapping import MutableMappingValidator
from .default_dict import DefaultDictValidator
from .ordered_dict import OrderedDictValidator
from .counter import CounterValidator
from .chain_map import ChainMapValidator
from .typed_dict import TypedDictValidator
from .user_dict import UserDictValidator


__all__ = [

    # Dict je základní a nejběžnější implementace slovníku.
    "DictValidator",

    # Mapping a MutableMapping jsou abstraktní rozhraní - vhodné pro parametry funkcí.
    "MappingValidator",
    "MutableMappingValidator",

    # DefaultDict, OrderedDict, Counter a ChainMap
    # jsou specializované implementace pro konkrétní případy použití.
    "DefaultDictValidator",
    "OrderedDictValidator",
    "CounterValidator",  # Definuje vlastní validační logiku
    "ChainMapValidator",  # Definuje vlastní validační logiku

    # TypedDict se výrazně liší tím, že nepřijímá generické typy K a V,
    # ale definuje konkrétní klíče a jejich typy.
    "TypedDictValidator",  # Definuje vlastní validační logiku

    # UserDict slouží jako základ pro vlastní implementace slovníků.
    "UserDictValidator"
]


