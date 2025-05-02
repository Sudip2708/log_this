import numpy as np
from typing import Annotated, Any, Dict, Optional, Tuple, Union

from ...._bases import BaseCustomLogicValidator
from ...._verifiers import numpy_array_verifier


class NumpyArrayValidator(BaseCustomLogicValidator):
    """
    Validátor pro typovou anotaci numpy.ndarray

    NumPy ndarray je mnohorozměrné (n-dimenzionální) pole, které poskytuje efektivní
    uložení a manipulaci s velkými objemy dat stejného typu. Oproti standardním
    strukturám Pythonu (list, tuple) poskytuje ndarray výrazně vyšší výkon pro
    numerické operace a podporuje pokročilé matematické a statistické funkce.

    Syntaxe:
        - np.ndarray                # Základní reference na typ ndarray
        - numpy.ndarray             # Plně kvalifikovaný zápis
        - Annotated[np.ndarray, {   # S metadaty pro dtype a tvar (experimentální)
              'dtype': np.float64,
              'shape': (3, 4)
          }]

    Datové typy (dtype):
        NumPy poskytuje širokou škálu datových typů:
        - np.int8, np.int16, np.int32, np.int64 - Celá čísla různých velikostí
        - np.uint8, np.uint16, np.uint32, np.uint64 - Neznaménková celá čísla
        - np.float16, np.float32, np.float64 - Čísla s plovoucí desetinnou čárkou
        - np.complex64, np.complex128 - Komplexní čísla
        - np.bool_ - Booleovské hodnoty
        - np.object_ - Pythonové objekty
        - np.string_, np.unicode_ - Řetězce pevné délky

    Tvar pole (shape):
        Tvar pole určuje jeho dimenze:
        - (n,) - 1D pole délky n
        - (n, m) - 2D pole (matice) o n řádcích a m sloupcích
        - (n, m, k) - 3D pole

    Specifikace tvaru v anotacích:
        - (3, 4)     # Přesná specifikace: přesně 3 řádky a 4 sloupce
        - (3, None)  # Částečná specifikace: 3 řádky, libovolný počet sloupců
        - (...)      # Libovolný tvar
        - (3, ...)   # První dimenze je 3, zbytek libovolný

    Příklady použití:
        - np.array([1, 2, 3])                      # 1D pole
        - np.zeros((3, 4))                         # 2D pole nul
        - np.arange(10).reshape(2, 5)              # 2D pole z rozsahu 0-9
        - Annotated[np.ndarray, {'dtype': np.int32}]  # Anotace pro pole celých čísel

    Validační proces:
        1. Validátor ověří, zda hodnota je instance typu numpy.ndarray.
        2. Pokud je použita anotace Annotated s metadaty, validuje se:
           a) dtype pole - zda odpovídá očekávanému datovému typu
           b) tvar pole (shape) - zda odpovídá očekávanému tvaru

    Použití v kódu:
        - Základní: 
          def process_array(data: np.ndarray) -> None: ...

        - S kontrolou dtype a tvaru:
          IntMatrix = Annotated[np.ndarray, {'dtype': np.int32, 'shape': (None, 3)}]
          def process_matrix(data: IntMatrix) -> None: ...

    Výhody oproti standardním strukturám:
        - Vysoký výkon pro vektorové a maticové operace
        - Efektivní uložení homogenních dat
        - Bohatá sada matematických a statistických funkcí
        - Podpora pokročilých indexovacích technik (fancy indexing)
        - Efektivní broadcasting operací

    Omezení:
        - Všechny prvky musí mít stejný datový typ (homogenní pole)
        - Změna tvaru nemění hodnoty, pouze jejich uspořádání
        - Vyšší paměťová režie pro velmi malé pole

    Kdy použít:
        - Pro efektivní zpracování velkých objemů numerických dat
        - Pro matematické a statistické výpočty
        - Pro práci s vícerozměrnými daty (obrazy, signály, časové řady)
        - Pro integraci s nízkoúrovňovými C/Fortran knihovnami

    Běžné chyby:
        - Zapomenutí importu: import numpy as np
        - Záměna seznamu a numpy array (rozdílné chování)
        - Nesprávné pochopení broadcastingu
        - Nevhodné použití dtype (např. np.int8 pro velká čísla)
        - Vytvoření kopie místo pohledu (view) na data

    Reference:
        - https://numpy.org/doc/stable/reference/arrays.ndarray.html
        - https://numpy.org/doc/stable/reference/arrays.dtypes.html
    """

    VALIDATOR_KEY = "numpy_ndarray"
    ANNOTATION = np.ndarray
    INFO = "Definuje objekt typu numpy.ndarray"
    ORIGIN = np.ndarray

    def __call__(
            self,
            value: Any,
            annotation: Any,
            depth_check: Union[bool, int],
            custom_types: dict = None,
            bool_only: bool
    ) -> Union[bool, Any]:
        """
        Provádí validaci hodnoty proti typu numpy.ndarray s možností kontroly dtype a tvaru.

        Základní kontrola ověří, zda je hodnota instancí numpy.ndarray.
        Rozšířená kontrola při použití Annotated s metadaty validuje dtype a tvar pole.

        Args:
            value (Any): Vstupní hodnota k validaci.
            annotation (Any): Typová anotace, např. `np.ndarray`, 
                             `Annotated[np.ndarray, {'dtype': np.float64, 'shape': (3, 4)}]`.
            depth_check (Union[bool, int]): Hloubka kontroly nebo True/False.
            custom_types (Tuple[Any, ...]): N-tice uživatelsky definovaných typů.
            bool_only (bool): Pokud je True, výstup je pouze True/False; jinak se vrací výjimka při chybě.

        Returns:
            bool | Any: True při úspěšné validaci, jinak vyvolá výjimku nebo vrátí False.
        """
        return numpy_array_verifier(
            value, self.ORIGIN, annotation, depth_check, bool_only
        )