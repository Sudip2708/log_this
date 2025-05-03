from typing import ForwardRef

from ...._bases import BaseIsInstanceValidator


class ForwardRefValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci ForwardRef

    ForwardRef umožňuje odkazovat na typy, které ještě nebyly definovány v okamžiku
    vytvoření typové anotace. Tento mechanismus řeší problém kruhových závislostí a
    umožňuje vytvářet rekurzivní datové struktury v typovém systému Pythonu.

    Syntaxe:
        - ForwardRef('TypeName')                # Explicitní konstrukce
        - 'TypeName'                            # Implicitní použití v anotacích
        - from __future__ import annotations    # Automatické použití pro všechny anotace

    Příklady použití:
        - List[ForwardRef('Tree')]              # Explicitní použití v rekurzivním typu
        - Tree = List['Tree']                   # Implicitní použití v rekurzivním typu
        - class Node: next: 'Node' = None       # Reference na třídu v té samé třídě

    Validační proces:
        1. Ověří, zda hodnota je instance typu ForwardRef
        2. ForwardRef je zpravidla jen přechodná reprezentace typu a měla by být
           rozpoznána a nahrazena konkrétním typem během typové kontroly

    Použití v kódu:
        - Pro rekurzivní datové struktury:
          ```python
          class TreeNode:
              value: int
              children: List['TreeNode']  # ForwardRef na vlastní třídu
          ```
        - Pro kruhové závislosti mezi moduly:
          ```python
          # V module a.py
          from typing import List
          from __future__ import annotations
          import b  # Importováno dole kvůli kruhové závislosti

          class A:
              bs: List[b.B]  # B ještě není definováno, ale funguje

          import b  # Skutečný import
          ```

    Specifické informace:
        - Od Python 3.7: ForwardRef se vyhodnocuje při volání get_type_hints()
        - Od Python 3.10: ForwardRef se vyhodnocuje automaticky, pokud je možné
        - S importem from __future__ import annotations se všechny anotace chovají jako
          ForwardRef a jsou uloženy jako řetězce

    Běžné chyby:
        - Neresolving ForwardRef: ForwardRef musí být nakonec nahrazen skutečným typem
        - Překlepy v názvu typu: 'UserMdoel' místo 'UserModel' způsobí runtime chybu
        - Používání ForwardRef bez potřeby: Pro běžné typy bez kruhových závislostí
          je lepší použít přímý odkaz na typ

    Reference:
        - https://docs.python.org/3/library/typing.html#typing.ForwardRef
        - https://peps.python.org/pep-0484/#forward-references
        - https://peps.python.org/pep-0563/ (odložené vyhodnocení anotací)
    """

    VALIDATOR_KEY = "forwardref"
    ANNOTATION = ForwardRef  # ForwardRef('MyType')

    IS_INSTANCE = ForwardRef
    DUCK_TYPING = None

    DESCRIPTION = "Dopředná reference na typ"
    LONG_DESCRIPTION = (
            "Validuje, že typ je ForwardRef, což umožňuje používat typové anotace "
            "pro typy, které ještě nebyly definovány, "
            "typicky při vzájemných referencích mezi třídami."
        )
