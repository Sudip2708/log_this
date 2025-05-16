from typing import Any, get_origin, Optional, Callable
from .end_verifiers import is_instance_verifier

import functools


class TypingValidator:

    def __call__(
            self,
            value: Any,  # Hodnota která se má ověřit
            annotation = None,  # Typová onotace podle které se má ověřit
            custom_types = None,  # Specifikace vlastních typů, a tříd, předaných jako tuple pro kontrolu vzorů
            inner_check=True,  # Parametr nastavující zda se má provádět i hloubková kontrola (a jak moc hluboko)
            duck_typing = False,  # Nastavení zda se má provádět kontrola jen na základě duck typing porovnání
            bool_only = False  # Specifkace zda vyvysovat neshody jako výjimky a nebo jen vracet false
        ):
            """Hlavní funkce pro validaci na základě typových anotací"""

            try:

                # Přednostní vyřízení nativních typů
                # Nativní typy neobsahují vnitřní prvky a tak se hned vracejí
                # (nevstahuje se na ně ani ověření přes duck typing a ani přes předané vlastní typi)
                if isinstance(annotation, type):
                    return is_instance_verifier(value, annotation, bool_only)

                # Získání validační třídy
                # Pokud byla získána validační třídy
                # Volání validační logiky definované pro danou anotaci
                validate_class = self.get_validate_class(annotation)
                if validate_class:
                    return validate_class(value, annotation, custom_types, duck_typing, inner_check, bool_only)

                # Pokud validační třída pro anotaci nebyla nalezena
                # Kontrola zda je přidán parametr pro vlastní anotace (klíčem slovníku)
                # Validace na základě předaných dat
                if custom_types and annotation in custom_types:
                    return custom_types_verifier(value, custom_types[annotation], duck_typing, inner_check, bool_only)

                # Pokud nebyla anotace zachycena, dojde k ověření zda nemá implementované validační metody
                # Self validátor by měla být funkce která se pokusí prohledat objekt na všechny možné způsoby nastavení sebevalidace
                # Když selže vyvolá výjimku která se pak zpracuje vě větvi except
                return self_validator(value, annotation, bool_only)


            # Propagace vnitřní výjimky
            # Zachytávat výjimky podle způsobu dalšího vyřízení využít bool_only
            except ValueError:
                raise

            # Zachycení všech neočekávaných výjimek
            except Exception as e:
                raise VerifyUnexpectedInternalError(e) from e


    @staticmethod
    @functools.lru_cache(maxsize=1024)
    def get_annotation_key(annotation) -> str:
        """Vrací zjednodušený klíč typu z anotace pomocí split metod."""
        s = str(annotation)
        s = s.split('[', 1)[0]
        s = s.rsplit('.', 1)[-1]
        return s.strip().lower()

    def get_validate_class(self, annotation) -> 'Optional[Callable]':
        """Vrací validační třídu podle anotace (nejprve přes `origin`, pak podle klíče)."""
        return (self.get_origin_validate_class(annotation)
                or self.get_key_validate_class(annotation))

    @staticmethod
    def get_origin_validate_class(annotation) -> 'Optional[Callable]':
        """Vrací validační třídu na základě generického typu (např. list, dict)."""
        origin = get_origin(annotation)
        return validators_orig_dict.get(origin) if origin else None

    def get_key_validate_class(self, annotation) -> 'Optional[Callable]':
        """Vrací validační třídu podle řetězcového klíče."""
        key = self.get_annotation_key(annotation)
        return validators_dict.get_item(key, None)



typing_validator = TypingValidator()