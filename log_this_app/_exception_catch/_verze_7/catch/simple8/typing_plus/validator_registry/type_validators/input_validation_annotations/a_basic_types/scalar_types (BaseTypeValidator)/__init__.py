"""
### 📂 `a_basic_scalar_types`
**Popis**:
Jedná se o validační třídy pro _základní skalární typy_, které se dají přímo použít pro anotaci vstupu – tedy hodnoty, které nejsou kontejner nebo abstrakce, ale samostatné, atomické hodnoty.

---

#### ✅ Obsah složky:

| Soubor | Zhodnocení |
|--------|------------|
| `__init__.py` | ✅ Bez problému. |
| `bool.py` | ✅ Základní atomický typ – patří sem. |
| `complex.py` | ✅ Typ `complex` je standardní a atomický – sem patří. |
| `float.py` | ✅ Patří sem. |
| `int.py` | ✅ Patří sem. |
| `str.py` | ✅ Patří sem. |
| `none.py` | 🔶 Lehce diskutabilní – viz níže. |

"""
from .bool import BoolValidator
from .complex import ComplexValidator
from .float import FloatValidator
from .int import IntValidator
from .str import StrValidator
from .none import NoneValidator

from ..._utils import get_package_dict, get_package_names

package = (
    BoolValidator,
    ComplexValidator,
    FloatValidator,
    IntValidator,
    StrValidator,
    NoneValidator
)

scalar_types_dict = get_package_dict(package)

__all__ = ["scalar_types_dict"] + get_package_names(package)

