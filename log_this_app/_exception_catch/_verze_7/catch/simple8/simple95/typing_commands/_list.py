"""
List[Any]                       # univerzální typ, cokoliv
List[Union[int, str]]          # unie více typů
List[Optional[int]]            # Optional je alias pro Union[X, None]
List[Literal["a", "b", 1]]     # omezený výčet hodnot
List[Annotated[int, "meta"]]   # typ s dodatečnou anotací
List[Callable[[int], str]]     # funkce s typy argumentů a návratovou hodnotou
List[TypeVar("T")]             # generický typový parametr
List[Final[int]]               # konstantní hodnota
List[ClassVar[int]]            # proměnná třídy (většinou jen v rámci datových tříd)
List[ForwardRef("MyClass")]    # odkazy na budoucí definici
List["MyClass"]                # běžný stringový forward ref
List[NewType("UserId", int)]   # vlastní typ alias

"""
from typing import Any, List, Union, get_args
import traceback

from ..typing_validate_error import TypingValidateError
from ..validate_native_type import validate_native_type
from ..validator import validator

# Definice typové anotace pro typové anotace knihovny typing
TypingAnnotation = Any

class ListMixin(ABC):

    def _list(
            self,
    ):
        try:

            # Validace hodoty (vyvolá výjimku v případě nevalidní hodnoty)
            validate_native_type(self.value, list)

            # Pokud není požadavek na vnitřní kontrolu (a nebo je již vyčerpaná) vraď True
            if not self.inner_check:
                return True

            # Získání vnitřní anotace:
            item_annotation = get_args(self.type_annotation)

            # Ověření vnitřních položek
            for item in self.value:

                # Korekce hodnoty inner_check, a případné vrácení True při jejím vyčerpání
                # (Kompaktní zápis kvůli častému výskytu; standardní forma by byla neúměrně rozvleklá)
                if isinstance(self.inner_check, int):
                    if self.inner_check > 0: self.inner_check -= 1
                    else: return True

                # Validace položky
                self.validator(self.item, item_annotation, self.inner_check)

        # Zachycení výjimky z volaných funkcí
        except TypingValidateError as e:
            # process_existing_exeption(e)  # Funkce spracuje již existující výjimku, něco k ní dopíše
            raise TypingValidateError(
                f"Chyba ověření vnitřních položek seznamu: {str(e)}"
            ) from e



        # # Zamyslet se nad strukturou výjimek a vytvořit jen přidánívání předfixu
        # except TypingValidateError as e:
        #     raise TypingValidateError(
        #         f"[_list()]: {str(e)}"
        #     ) from e

        # Zachycení všech nečekaných výjimek
        except Exception as e:
            # create_new_exception(  # Funkce vytvoří novou výjimku
            #     e,
            #     traceback.extract_tb(e.__traceback__)[-1],
            #     message = "str"
            # )
            tb = traceback.extract_tb(e.__traceback__)[-1]
            raise TypingValidateError(
                f"Neočekávaná chyba při ověření obsahu seznamu. "
                f"Funkce: _list(value, type_annotation, inner_check). "
                f"Vstupní parametry: value={value}, type_annotation={type_annotation}, inner_check={inner_check}. \n"
                f"Popis chyby: {e.__class__.__name__} - {str(e)}. \n"
                f"Soubor: {tb.filename}. "
                f"Řádek: {tb.lineno}. "
                f"Kod: {tb.line}. \n"
            )








