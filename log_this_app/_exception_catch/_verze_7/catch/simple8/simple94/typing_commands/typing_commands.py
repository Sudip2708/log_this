from ._list import _list
from ._tuple import _tuple
from ._union import _union


# Slovník s příkazy
TYPING_COMMANDS = {
    "tuple": lambda c, v, e, i: _tuple(c, v, e, i),
    "list": lambda c, v, e, i: _list(c, v, e, i),
    "union": lambda c, v, e, i: _union(c, v, e, i),

}