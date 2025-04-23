from collections import UserList

from ..._bases import BaseIterableValidator, T


class UserListValidator(BaseIterableValidator):
    """
    Validátor pro typovou anotaci UserList[T]

    UserList je speciální třída ze standardní knihovny collections, která obaluje
    vestavěný seznam (list) a poskytuje rozhraní pro jeho rozšíření a přizpůsobení.
    Je primárně určena pro vytváření vlastních seznamových tříd děděním.

    Syntaxe:
        - UserList[T]           # Typová anotace pro UserList s prvky typu T
        - collections.UserList[T]  # Plně kvalifikovaný zápis

    Příklady použití:
        - UserList[int]         # UserList obsahující celá čísla
        - UserList[str]         # UserList obsahující řetězce
        - UserList[Dict[str, Any]]  # UserList obsahující slovníky

    Vnitřní typy:
        Parametr T určuje typ prvků uložených v UserList. Může jít o jakýkoli
        validní Python typ včetně složených typů.

    Validační proces:
        1. Ověření, zda hodnota je instance collections.UserList
        2. Při hloubkové kontrole ověření typů všech prvků v seznamu
        3. Rekurzivní validace vnořených typů podle specifikace v depth_check

    Použití v kódu:
        - Pro parametry funkcí: def process_items(items: UserList[int]) -> None
        - Pro návratové hodnoty: def create_list() -> UserList[str]
        - Vytvoření vlastní třídy:
          ```
          class MyList(UserList[int]):
              def sum(self) -> int:
                  return sum(self.data)
          ```

    Vztah k jiným typům:
        - UserList implementuje stejné rozhraní jako vestavěný list
        - Na rozdíl od list má oddělené vnitřní úložiště (self.data)
        - Podobný UserDict a UserString, které umožňují přizpůsobení slovníků a řetězců

    Implementační detaily:
        - UserList ukládá svá data v atributu self.data jako běžný Python list
        - Deleguje většinu operací na tento vnitřní seznam
        - Poskytuje hooks pro přepsání základních operací

    Běžné chyby:
        - Záměna s běžným seznamem (list) při validaci
        - Zapomenutí na potřebu importu z collections
        - Přímý přístup k self.data místo použití rozhraní UserList

    Reference:
        - https://docs.python.org/3/library/collections.html#collections.UserList
        - https://docs.python.org/3/library/typing.html#user-defined-generic-types
    """

    VALIDATOR_KEY = "userlist"
    ANNOTATION = UserList[T]
    INFO = "Definuje přizpůsobitelný seznam založený na UserList"
    ORIGIN = UserList