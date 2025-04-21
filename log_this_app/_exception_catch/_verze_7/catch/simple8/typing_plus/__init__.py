"""
typing_plus/
│
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── validator.py          # validace všech typů (List, Tuple, Dict, vlastní třídy)
│   ├── dispatcher.py         # směrování na správný validátor podle typu
│   ├── decorator.py          # @validate_types
│   ├── errors.py             # vlastní výjimky + chybové zprávy
│   └── settings.py           # režimy validace, např. hloubka, výstup, only=True/False
│
├── types/
│   ├── __init__.py
│   ├── list_plus.py          # přetížení List s __validate__
│   ├── tuple_plus.py         # přetížení Tuple s __validate__
│   ├── union_plus.py         # Union s validací
│   └── class_wrapper.py      # ValidatedClass wrapper
│
├── tools/
│   ├── __init__.py
│   ├── validate_func.py      # ruční validace konkrétní hodnoty
│   ├── type_utils.py         # např. get_origin(), is_union_type() atd.
│   └── cast_utils.py         # budoucí: typová konverze, pokud to dává smysl
│
└── examples/
    └── basic_usage.py        # ukázky použití, výstup, režimy, own types
"""
