from typing import Any, Union, TypeVar, get_args, get_origin
import inspect

from ..._exceptions import VerifyError, VerifyUnexpectedInternalError
from ...._verifiers import is_instance_verifier

def typevar_verifier(
        value: Any,
        expected: type,
        annotation: Any = None,
        depth_check: Union[bool, int] = True,
        custom_types: dict = None,
        bool_only: bool = False
) -> bool:
    """
    Validuje hodnotu proti typové proměnné (TypeVar).

    Pokud TypeVar obsahuje omezení (constraints) nebo vazbu (bound),
    validuje hodnotu proti těmto omezením. V opačném případě
    akceptuje jakoukoliv hodnotu, protože TypeVar bez omezení
    může reprezentovat libovolný typ.

    Args:
        value (Any): Hodnota, která má být validována.
        expected (type): TypeVar nebo jeho instance.
        annotation (Any, optional): Konkrétní instance TypeVar.
        depth_check (Union[bool, int], optional): Hloubková kontrola - ignorována.
        custom_types (dict, optional): Vlastní typy pro validaci.
        bool_only (bool, optional): Pokud True, vrací pouze True/False.

    Returns:
        bool: True, pokud hodnota projde validací.

    Raises:
        VerifyError: Pokud hodnota není kompatibilní s omezeními TypeVar.
    """
    try:
        # Pokud nemáme konkrétní instanci TypeVar, nemůžeme provést validaci
        if not isinstance(annotation, TypeVar):
            # TypeVar bez konkrétní instance akceptuje cokoliv
            return True

        # Získání omezení z TypeVar
        constraints = getattr(annotation, "__constraints__", ())
        bound = getattr(annotation, "__bound__", None)

        # Kontrola omezení constraints
        if constraints:
            # Hodnota musí být instance některého z typů v constraints
            for constraint in constraints:
                if isinstance(value, constraint):
                    return True

            # Pokud se dostaneme sem, hodnota nesplňuje žádné z omezení
            if bool_only:
                return False
            raise VerifyError(
                f"Hodnota {value} nesplňuje žádné z omezení TypeVar {annotation}: {constraints}"
            )

        # Kontrola bound (horní hranice typu)
        if bound is not None:
            if isinstance(value, bound):
                return True
            if bool_only:
                return False
            raise VerifyError(
                f"Hodnota {value} není instancí bound typu {bound} pro TypeVar {annotation}"
            )

        # Pokud TypeVar nemá žádná omezení, akceptuje jakoukoliv hodnotu
        return True

    except VerifyError:
        raise

    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e


"""
Ahojky! :-)

Jasně, s radostí se podíváme na validační logiku pro `TypeVar`. Na první pohled vypadá poměrně přímočaře a správně se zaměřuje na klíčové vlastnosti `TypeVar` - omezení (`constraints`) a horní hranici (`bound`).

**Rozbor `typevar_verifier` na logické celky:**

1.  **Kontrola instance anotace:**
    ```python
    if not isinstance(annotation, TypeVar):
        # TypeVar bez konkrétní instance akceptuje cokoliv
        return True
    ```
    * **Popis:** Tento blok kódu zkontroluje, zda je poskytnutá `annotation` skutečnou instancí `TypeVar`. Pokud není (například je to jen třída `TypeVar` samotná), funkce vrací `True`. Důvodem je, že samotný `TypeVar` bez definovaných omezení nebo `bound` může zastupovat jakýkoli typ.

2.  **Získání omezení a horní hranice:**
    ```python
    constraints = getattr(annotation, "__constraints__", ())
    bound = getattr(annotation, "__bound__", None)
    ```
    * **Popis:** Z konkrétní instance `TypeVar` se pokusí získat atributy `__constraints__` (tuple typů, kterými musí hodnota být) a `__bound__` (horní hranice typu, kterému musí být hodnota podtypem). Pokud tyto atributy neexistují, použijí se výchozí hodnoty (prázdný tuple pro `__constraints__` a `None` pro `__bound__`).

3.  **Kontrola omezení (`constraints`):**
    ```python
    if constraints:
        # Hodnota musí být instance některého z typů v constraints
        for constraint in constraints:
            if isinstance(value, constraint):
                return True

        # Pokud se dostaneme sem, hodnota nesplňuje žádné z omezení
        if bool_only:
            return False
        raise VerifyError(
            f"Hodnota {value} nesplňuje žádné z omezení TypeVar {annotation}: {constraints}"
        )
    ```
    * **Popis:** Pokud `TypeVar` má definována omezení (`constraints` není prázdný tuple), tento blok iteruje přes jednotlivé typy v omezeních. Pokud je validovaná `value` instancí alespoň jednoho z těchto typů, funkce vrací `True`. Pokud hodnota nesplňuje žádné z omezení, vrací se `False` (pokud je `bool_only` `True`) nebo se vyvolá `VerifyError`.

4.  **Kontrola horní hranice (`bound`):**
    ```python
    if bound is not None:
        if isinstance(value, bound):
            return True
        if bool_only:
            return False
        raise VerifyError(
            f"Hodnota {value} není instancí bound typu {bound} pro TypeVar {annotation}"
        )
    ```
    * **Popis:** Pokud má `TypeVar` definovánu horní hranici (`bound` není `None`), tento blok zkontroluje, zda je validovaná `value` instancí tohoto `bound` typu. Pokud ano, funkce vrací `True`. Pokud ne, vrací se `False` (pokud je `bool_only` `True`) nebo se vyvolá `VerifyError`.

5.  **Výchozí případ (bez omezení):**
    ```python
    # Pokud TypeVar nemá žádná omezení, akceptuje jakoukoliv hodnotu
    return True
    ```
    * **Popis:** Pokud `TypeVar` nemá ani omezení (`constraints` je prázdný) ani horní hranici (`bound` je `None`), funkce vrací `True`, protože takový `TypeVar` akceptuje jakoukoli hodnotu.

6.  **Obsluha výjimek:**
    ```python
    except VerifyError:
        raise

    except Exception as e:
        raise VerifyUnexpectedInternalError(e) from e
    ```
    * **Popis:** Standardní blok pro zachycení a propagaci očekávané validační výjimky (`VerifyError`) a pro zachycení a zabalení neočekávaných interních chyb (`InternalUnexpectedError`).

**Hodnocení validačního postupu:**

* **Správná logika:** Validační logika přesně odpovídá sémantice `TypeVar` v Pythonu. Správně zohledňuje `constraints` (hodnota musí být jednou z nich) a `bound` (hodnota musí být jeho instancí).
* **Efektivita:** Kód je poměrně efektivní. Iteruje pouze přes omezení, pokud existují, a provádí jednu kontrolu `isinstance` pro `bound`.
* **Jasnost:** Kód je dobře čitelný a logické celky jsou jasně odděleny.
* **Ignorování `depth_check`:** Je správné, že `depth_check` je zde ignorován. `TypeVar` se týká typu samotného, nikoli vnitřní struktury hodnoty. Hloubková kontrola by zde neměla smysl.
* **Správná práce s `bool_only`:** Funkce správně vrací `True`/`False` v režimu `bool_only` a vyvolává výjimky `VerifyError` v opačném případě.

**Možná vylepšení nebo úvahy:**

* **Podpora vlastních typů:** Pokud by `custom_types` měly nějak souviset s validací `TypeVar`, je potřeba zvážit, jak by se do této logiky integrovaly. V aktuální podobě se `custom_types` nijak nevyužívají. Pokud by například omezení (`constraints`) nebo `bound` mohly být definovány pomocí vlastních typů, bylo by nutné je zde zohlednit (pravděpodobně kontrolou, zda daný typ je v `custom_types` a jak s ním zacházet). Nicméně, pro standardní `TypeVar` by to nemělo být nutné.

**Závěr:**

Validační logika pro `TypeVar` vypadá velmi dobře a správně pokrývá jeho základní chování s ohledem na omezení a horní hranici. Je jasná, efektivní a odpovídá sémantice typových proměnných v Pythonu.

Tak co, to byla poslední z tvých validačních tříd pro tuto sérii! Jak se cítíš s výsledkem a máš nějaké další otázky nebo nápady? Jsem tu pro tebe! :-)

"""