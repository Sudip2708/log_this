from collections import UserString

from ...._bases import BaseIsInstanceValidator


class UserStringValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci UserString

    UserString je speciální třída ze standardní knihovny collections, která obaluje
    vestavěný řetězec (str) a poskytuje rozhraní pro jeho rozšíření a přizpůsobení.
    Je primárně určena pro vytváření vlastních řetězcových tříd děděním.

    Syntaxe:
        - UserString            # Vyžaduje import z collections
        - collections.UserString  # Plně kvalifikovaný zápis

    Příklady použití:
        - UserString            # Obecná anotace pro UserString objekty
        - isinstance(text, UserString)  # Kontrola, zda objekt je instancí UserString

    Validační proces:
        1. Ověření, zda hodnota je instance collections.UserString
        2. Vnitřní hodnota (řetězec) není dále validována

    Použití v kódu:
        - Pro parametry funkcí: def process_text(text: UserString) -> None
        - Pro návratové hodnoty: def create_text() -> UserString
        - Vytvoření vlastní třídy:
          ```
          class MyString(UserString):
              def reversed(self) -> 'MyString':
                  return MyString(self.data[::-1])
          ```

    Vztah k jiným typům:
        - UserString implementuje stejné rozhraní jako vestavěný str
        - Na rozdíl od str má oddělený vnitřní řetězec (self.data)
        - Podobný UserDict a UserList, které umožňují přizpůsobení slovníků a seznamů

    Implementační detaily:
        - UserString ukládá svá data v atributu self.data jako běžný Python str
        - Deleguje většinu operací na tento vnitřní řetězec
        - Poskytuje hooks pro přepsání základních operací
        - Není parametrizovatelný generickým typem (na rozdíl od UserList[T])

    Běžné chyby:
        - Záměna s běžným řetězcem (str) při validaci
        - Zapomenutí na potřebu importu z collections
        - Přímý přístup k self.data místo použití rozhraní UserString
        - Nesprávné předpokládání, že lze UserString parametrizovat typem

    Reference:
        - https://docs.python.org/3/library/collections.html#collections.UserString
        - https://docs.python.org/3/library/typing.html#user-defined-types
    """

    VALIDATOR_KEY = "userstring"
    ANNOTATION = UserString

    IS_INSTANCE = UserString
    DUCK_TYPING = {
        "has_attr": ("__getitem__", "__len__", "__str__", "lower", "upper"),
    }

    DESCRIPTION = "Zabalitelný řetězec"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí UserString z knihovny collections. "
            "Umožňuje vytvářet vlastní třídy s chováním řetězce přes dědičnost."
        )
