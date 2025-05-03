import pandas as pd
from typing import Any, Union

from ...._bases import BaseCustomLogicValidator
from ...._verifiers import pandas_dataframe_verifier


class DataFrameValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci pandas.DataFrame

    DataFrame je dvourozměrná označená tabulková datová struktura s potenciálně heterogenními sloupci.
    Spojuje funkcionalitu SQL tabulek a spreadsheetů s možnostmi manipulace a analýzy dat
    pomocí jednoduchého a výkonného API. Umožňuje efektivní práci s rozsáhlými daty
    a jejich transformaci.

    Syntaxe:
        - pd.DataFrame             # Základní reference na typ DataFrame
        - pandas.DataFrame         # Plně kvalifikovaný zápis
        - Annotated[pd.DataFrame, {   # S metadaty pro kontrolu sloupců (experimentální)
              'columns': ['jméno', 'věk', 'město'],
              'dtypes': {'jméno': 'object', 'věk': 'int64', 'město': 'object'}
          }]

    Struktura DataFrame:
        - Index: Označení řádků, může být různých typů (integer, string, datetime, multi-index)
        - Columns: Označení sloupců, obvykle jako seznam názvů
        - Data: Skutečné hodnoty uložené v DataFrame

    Datové typy sloupců:
        DataFrame umožňuje mít různé datové typy v různých sloupcích:
        - int64, float64: Numerické typy
        - object: Obecné objekty, často řetězce
        - bool: Booleovské hodnoty
        - datetime64: Časové údaje
        - category: Kategorické hodnoty
        - string: Textové hodnoty (od pandas 1.0.0)

    Příklady použití:
        - pd.DataFrame({'A': [1, 2], 'B': [3, 4]})  # Ze slovníku
        - pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])  # Z 2D seznamu
        - pd.read_csv('data.csv')  # Načtení z CSV souboru
        - pd.read_excel('data.xlsx')  # Načtení z Excel souboru

    Validační proces:
        1. Validátor ověří, zda hodnota je instance typu pandas.DataFrame.
        2. Pokud je použita anotace Annotated s metadaty, validuje se:
           a) Přítomnost požadovaných sloupců
           b) Datové typy sloupců (pokud jsou specifikovány)

    Použití v kódu:
        - Základní:
          def process_data(data: pd.DataFrame) -> None: ...

        - S kontrolou sloupců:
          UserDF = Annotated[pd.DataFrame, {'columns': ['jméno', 'věk']}]
          def process_users(data: UserDF) -> None: ...

    Výhody oproti jiným datovým strukturám:
        - Integrace SQL-like operací a spreadsheet-like funkcí
        - Efektivní práce s chybějícími hodnotami (NaN)
        - Rychlé operace na velkých datových množinách
        - Snadná manipulace s daty (filtrování, agregace, pivotace)
        - Přímá integrace s dalšími knihovnami (matplotlib, scikit-learn)

    Operace s DataFrame:
        - Selekce: df['sloupec'], df.loc[], df.iloc[]
        - Filtrace: df[df['sloupec'] > 10]
        - Agregace: df.groupby('skupina').mean()
        - Spojování: pd.merge(df1, df2), df1.join(df2)
        - Transformace: df.apply(), df.map()

    Kdy použít:
        - Pro analýzu strukturovaných dat
        - Pro statistické výpočty a vizualizace
        - Pro čištění a transformaci dat
        - Pro práci s časovými řadami
        - Pro strojové učení a datovou vědu

    Běžné chyby:
        - Zapomenutí importu: import pandas as pd
        - Nesprávný přístup k datům (chained indexing)
        - Neočekávané vytváření kopií místo pohledů
        - Nedostatečné ošetření chybějících hodnot
        - Nesprávné pochopení indexu a jeho významu

    Reference:
        - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
        - https://pandas.pydata.org/docs/user_guide/dsintro.html
    """

    VALIDATOR_KEY = "DataFrame"
    ANNOTATION = pd.DataFrame

    IS_INSTANCE = pd.DataFrame
    DUCK_TYPING = {
        "has_attr": ("index", "columns", "shape", "dtypes", "loc", "iloc"),
        "has_callable_attr": ("groupby", "head"),
        "lambda": lambda obj: (
                isinstance(getattr(obj, "shape"), tuple)
                and len(getattr(obj, "shape")) == 2
        )
    }

    DESCRIPTION = "Dvourozměrná tabulková struktura (Pandas)"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí pandas.DataFrame, "
            "tedy dvourozměrné tabulky s označenými osami. "
            "Umožňuje manipulaci s heterogenními daty v řádcích "
            "a sloupcích s podporou operací jako spojování nebo filtrování."
        )

    def __call__(
            self,
            value: Any,
            annotation: Any,
            depth_check: Union[bool, int],
            custom_types: dict = None,
            bool_only: bool
    ) -> Union[bool, Any]:

        return pandas_dataframe_verifier(
            value, self.ORIGIN, annotation, depth_check, bool_only
        )