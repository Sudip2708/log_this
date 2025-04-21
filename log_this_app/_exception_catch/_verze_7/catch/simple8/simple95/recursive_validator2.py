from typing import Any, Callable, Dict, List, Union
import typing

from .typing_validate_error import TypingValidateError
from .isinstance_types_dict import ISINSTANCE_TYPES

# Definice typové anotace pro typové anotace knihovny typing
TypingAnnotation = Any


class RecursiveValidatorMixin(ABC):


    def recursive_validator(self):

        try:

            # Provedení ověření
            a, b, c, d, e = self.command(self.content, self.value, self.type_annotation, self.inner_check)
            self.command, self.content, self.value, self.type_annotation, self.inner_check = a, b, c, d, e

            # Ověření požadavku na vnitřní kontrolu
            if not self.inner_check or not self.content:
                return True

            # Rekurzivní volání pro hlubší úroveň porovnání
            self.recursive_validator()


        # Předání případné výjimky ověření
        except TypingValidateError:
            raise

        # Zachycení všech ostaních výjimek
        except Exception as e:
            raise TypingValidateError("Vnitřní chyba validace")