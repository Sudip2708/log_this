import pandas as pd
from typing import Any, Union

from ...._bases import BaseCustomLogicValidator
from ...._verifiers import pandas_series_verifier


class SeriesValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci pandas.Series

    Series je jednorozměrná označená datová struktura, která může obsahovat libovolný
    datový typ (celá čísla, řetězce, float, objekty, atd.). Lze ji chápat jako
    jednorozměrný array s pojmenovanými prvky nebo jako jeden sloupec DataFrame.
    Series kombinuje vlastnosti polí a slovníků, což ji činí velmi flexibilní
    a výkonnou datovou strukturou pro analýzu dat.

    Syntaxe:
        - pd.Series               # Základní reference na typ Series
        - pandas.Series           # Plně kvalifikovaný zápis
        - Annotated[pd.Series, {  # S metadaty pro další kontrolu (experimentální)
              'dtype': 'int64',
              'name': 'hodnoty'
          }]

    Struktura Series:
        - Index: Označení prvků, může být různých typů (integer, string, datetime)
        - Values: Skutečné hodnoty uložené v Series
        - Name: Volitelný název Series

    Datové typy:
        Series může obsahovat různé datové typy:
        - int64, float64: Numerické typy
        - object: Obecné objekty, často řetězce
        - bool: Booleovské hodnoty
        - datetime64: Časové údaje
        - category: Kategorické hodnoty
        - string: Textové hodnoty (od pandas 1.0.0)

    Příklady použití:
        - pd.Series([1, 2, 3])  # Ze seznamu
        - pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # Se specifikovaným indexem
        - pd.Series({'a': 1, 'b': 2, 'c': 3})  # Ze slovníku
        - df['sloupec']  # Jako sloupec DataFrame

    Validační proces:
        1. Validátor ověří, zda hodnota je instance typu pandas.Series.
        2. Pokud je použita anotace Annotated s metadaty, validuje se:
           a) Datový typ Series (dtype)
           b) Název Series (name), pokud je specifikován

    Použití v kódu:
        - Základní:
          def process_values(data: pd.Series) -> None: ...

        - S kontrolou typu:
          IntSeries = Annotated[pd.Series, {'dtype': 'int64'}]
          def process_numbers(data: IntSeries) -> None: ...

    Výhody oproti jiným datovým strukturám:
        - Kombinuje vlastnosti seznamů a slovníků
        - Efektivní práce s chybějícími hodnotami (NaN)
        - Bohatá sada integrovaných metod pro analýzu a manipulaci
        - Rychlé operace na velkých datových množinách
        - Snadná konverze mezi různými datovými typy

    Operace s Series:
        - Indexování: s['index'], s.iloc[0]
        - Filtrace: s[s > 10]
        - Agregace: s.sum(), s.mean(), s.describe()
        - Transformace: s.apply(), s.map()
        - Matematické operace: s * 2, s + s2, np.log(s)

    Kdy použít:
        - Pro práci s jednorozměrnými daty
        - Pro analýzu časových řad
        - Pro rychlé agregace a transformace dat
        - Jako mezikrok při zpracování dat v DataFrame
        - Pro uložení kategorických dat

    Běžné chyby:
        - Zapomenutí importu: import pandas as pd
        - Záměna Series a DataFrame (Series je jednorozměrná)
        - Nesprávné použití indexu
        - Nedostatečné ošetření chybějících hodnot
        - Nesprávná interpretace výsledků operací (mnoho operací vrací novou Series)

    Reference:
        - https://pandas.pydata.org/docs/reference/api/pandas.Series.html
        - https://pandas.pydata.org/docs/user_guide/dsintro.html#series
    """

    VALIDATOR_KEY = "Series"
    ANNOTATION = pd.Series

    IS_INSTANCE = pd.Series
    DUCK_TYPING = {
        "has_attr": ("index", "dtype", "shape", "size", "loc", "iloc"),
        "has_callable_attr": ("head", "value_counts"),
        "lambda": lambda obj: (
                isinstance(getattr(obj, "shape"), tuple)
                and len(getattr(obj, "shape")) == 1
                and isinstance(getattr(obj, "size"), int)
        )
    }

    DESCRIPTION = "Jednorozměrné označené pole (Pandas)"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí pandas.Series, "
            "tedy jednorozměrné kolekce dat s označenými indexy. "
            "Kombinuje vlastnosti NumPy polí s výhodami "
            "označených indexů a operací nad daty."
        )

    def __call__(
            self,
            value: Any,
            annotation: Any,
            depth_check: Union[bool, int],
            custom_types: dict = None,
            bool_only: bool
    ) -> Union[bool, Any]:

        return pandas_series_verifier(
            value, self.ORIGIN, annotation, depth_check, bool_only
        )