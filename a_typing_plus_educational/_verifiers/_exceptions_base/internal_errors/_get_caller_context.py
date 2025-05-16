import inspect
from typing import Tuple


def get_caller_context() -> Tuple[str, str]:
    """
    Získá jméno volající funkce a modulu, s možností přeskočit pomocné funkce.

    Tato funkce je interní a nastavena pouze pro zpracování výjimek.
    A vrací zpátky jméno funkce a modulu třetího rámce:
        1. je tato funkce,
        2. je výjimka která tuto funkci volá,
        3. je kod který vyvolal výjimku a který chceme zobrazit

    Falešné hlášení chybně definované návratové hodnoty (v PyCharm) je způsobeno
    použitím inspekt, ktré může vrátit i None, ale funkce jako taková
    vždy vrací tuple s dvouma stringy.
    """

    # Definice defaultních hodnot
    function_name = '<neznámá funkce>'
    module_name = '<neznámý modul>'

    # Získání aktuálního rámce zásobníku
    current_frame = inspect.currentframe()

    # Pokud se podařilo získat rámec, načteme kontext
    if current_frame:
        try:

            # Získání okolních rámců
            outer_frames = inspect.getouterframes(current_frame)

            # Výběr rámce volající funkce (2 úroveň nad tímto kódem -
            # 1. je tato funkce,
            # 2. je výjimka která tuto funkci volá,
            # 3. je kod který vyvolal výjimku a který chceme zobrazit)
            if len(outer_frames) > 2:
                outer_frame = outer_frames[2]

                # Získání názvu funkce
                function_name = outer_frame.function

                # Získání názvu modulu, je-li dostupný
                if outer_frame.frame:
                    module_name = outer_frame.frame.f_globals.get(
                        '__name__', module_name
                    )

        finally:
            # Explicitní uvolnění reference na rámec
            # pro prevenci problémů s referenčním počítáním
            del current_frame  # předejde únikům paměti

    return function_name, module_name
