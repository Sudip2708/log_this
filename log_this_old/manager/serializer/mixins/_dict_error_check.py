class DictErrorCheckMixin:

    def _dict_error_check(self, dictionary):
        """
        Kontroluje, zda slovník obsahuje oznam o chybě, a upravuje jeho strukturu.

        Tato metoda detekuje oznam o chybě ve vnořených slovnících a předává ho do vrchní úrovně.
        Zamezuje tak vzniku rekurzivních zanořených struktur, které by mohly vzniknout při sériových chybách.

        Metoda postupuje následovně:
        - Načte hodnotu prvního klíče slovníku.
        - Pokud je tato hodnota slovníkem, načte hodnotu jeho prvního klíče.
        - Pokud je tato vnořená hodnota řetězec začínající na `<SerializationError`, považuje ji za oznam o chybě.
        - Oznam o chybě přesune jako hodnotu pro aktuální klíč ve vrchním slovníku, čímž eliminuje další zanořování.

        Parametry:
            dictionary (dict): Slovník, který má být kontrolován. Očekává se, že obsahuje potenciální chyby
                               ve formě řetězců začínajících na `<SerializationError`.

        Návratová hodnota:
            dict: Upravený slovník, ve kterém je oznam o chybě (pokud byl nalezen) přenesen na vrchní úroveň
                  a odstraněno zanoření.

        Příklad použití:
            Předpokládejme slovník s vnořeným oznamem o chybě:

            data = {
                "key1": {
                    "key2": "<SerializationError: Example error message>"
                }
            }

            result = self._dict_error_check(data)
            print(result)

            Očekávaný výstup:
            {
                "key1": "<SerializationError: Example error message>"
            }

        Poznámky:
            - Metoda předpokládá, že první hodnota každého slovníku je relevantní pro kontrolu. Pokud je slovník
              prázdný nebo struktura neodpovídá očekávání, metoda jednoduše vrátí nezměněný slovník.
            - Účelem je zajistit, že oznamy o chybách nebudou rekurzivně zanořeny, což usnadňuje jejich zpracování.
        """

        # Načtení hodnoty pro první klíč
        value = next(iter(dictionary.values()))

        # Kontrola zda je hodnota slovníkem
        if isinstance(value, dict):

            # Načtení hodnoty pro první klíč vnořeného slovníku
            inner_value = next(iter(value.values()))

            #Kontrola zda je hodnota řetězec a obsahuje oznam o chybě
            if isinstance(inner_value, str) and inner_value.startswith("<SerializationError"):

                # Načtení klíče pro aktuální slovník a změna jeho hodnoty z vnořeného slovníku na oznam
                first_key = next(iter(dictionary))
                dictionary[first_key] = inner_value

        # Navrácení upraveného slovníku
        return dictionary