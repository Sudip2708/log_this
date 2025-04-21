import inspect
from typing import Callable, Dict, Any
import docformatter

from cli_interactive.abc_helper import abc_method


def abc_doc_generator(
        template: str = """
{method_name}

Abstraktní metoda vyžadující implementaci.

Parametry:
{parameters}

Návratová hodnota:
{return_type}

Raises:
    NotImplementedError: Při pokusu o přímé volání abstraktní metody.
"""
) -> Callable:
    """
    Dekorátor pro automatické generování dokumentace abstraktních metod.

    Výhody:
    - Automatické generování konzistentní dokumentace
    - Extrakce informací přímo z typových anotací
    - Jednotný formát dokumentace pro abstraktní metody

    Použití:
    1. Udržování konzistentní dokumentace
    2. Automatické generování podkladů pro API dokumentaci
    3. Usnadnění tvorby dokumentace

    Args:
        template: Šablona pro generování dokumentace

    Returns:
        Dekorovaná metoda s automaticky generovanou dokumentací
    """

    def decorator(func: Callable) -> Callable:
        # Extrakce informací o metodě
        sig = inspect.signature(func)
        type_hints = inspect.getfullargspec(func)

        # Generování popisu parametrů
        def format_parameters() -> str:
            params = []
            for name, param in sig.parameters.items():
                if name == 'self':
                    continue

                # Získání popisu typu
                type_str = type_hints.annotations.get(name, 'Any')

                # Formátování parametru
                param_desc = f"    {name} ({type_str}): Popis parametru"
                params.append(param_desc)

            return "\n".join(params) if params else "    Žádné parametry"

        # Generování popisu návratové hodnoty
        def format_return_type() -> str:
            return_annotation = type_hints.annotations.get('return', 'None')
            return f"{return_annotation}"

        # Generování dokumentace
        doc = template.format(
            method_name=func.__name__,
            parameters=format_parameters(),
            return_type=format_return_type()
        )

        # Formátování dokumentace (volitelné)
        try:
            doc = docformatter.format_docstring(doc)
        except ImportError:
            # Pokud není docformatter k dispozici, použije se nezformátovaný text
            pass

        # Přiřazení dokumentace
        func.__doc__ = doc

        return func

    return decorator


# # Příklad použití
# class DocumentedAbstractClass(ABC):
#
#     @abc_doc_generator()
#     @abstractmethod
#     def process_item(
#             self,
#             item: str,
#             weight: float,
#             optional: bool = False
#     ) -> Dict[str, Any]:
#         pass


