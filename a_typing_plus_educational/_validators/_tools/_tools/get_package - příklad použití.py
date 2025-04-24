"""
Validátory pro standardní kontejnerové typy v Pythonu.

Tento balíček obsahuje implementace validátorů pro základní kolekce a mapování,
které jsou součástí standardní knihovny Pythonu a mají podporu v modulu typing.

Obsažené validátory:
- Dict: Validátor pro slovníky (Dict[K, V])
- List: Validátor pro seznamy (List[T])
- Set: Validátor pro množiny (Set[T])
- FrozenSet: Validátor pro neměnné množiny (FrozenSet[T])
- Tuple: Validátor pro n-tice (Tuple[T1, T2, ...] a Tuple[T, ...])

Použití:
    # Použití jednotlivých validátorů
    from my_package.validators.containers import ListValidator

    validator = ListValidator()
    result = validator.validate([1, 2, 3], List[int], depth_check=True, custom_types={}, bool_only=False)

    # Použití slovníku validátorů
    from my_package.validators.containers import containers_dict

    # Získání validátoru podle klíče 
    list_validator = containers_dict["list"]
    result = list_validator.validate([1, 2, 3], List[int], depth_check=True, custom_types={}, bool_only=False)

Exportované objekty:
- Třídy validátorů: DictValidator, ListValidator, SetValidator, FrozenSetValidator, TupleValidator
- containers_dict: Slovník všech validátorů s klíči odpovídajícími jejich VALIDATOR_KEY

Všechny validátory v tomto balíčku implementují stejné rozhraní pro validaci
a jsou navrženy pro kontrolu hodnot proti odpovídajícím anotacím z modulu typing.

Související moduly:
- typing
- collections.abc
"""
from .dict import DictValidator
from .frozen_set import FrozenSetValidator
from .list import ListValidator
from .set import SetValidator
from .tuple import TupleValidator

from ..._utils import get_package_dict, get_package_names

package = (
    DictValidator,
    FrozenSetValidator,
    ListValidator,
    SetValidator,
    TupleValidator
)

basic_containers_dict = get_package_dict(package)

__all__ = ["basic_containers_dict"] + get_package_names(package)