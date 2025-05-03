from datetime import time

from ...._bases import BaseIsInstanceValidator


class TimeValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci datetime.time

    Typ datetime.time reprezentuje denní čas nezávislý na konkrétním datu,
    obsahující hodinu, minutu, sekundu, mikrosekundu a volitelně informaci
    o časovém pásmu.

    Syntaxe:
        - datetime.time       # Vyžaduje import `from datetime import time`

    Příklady použití:
        - datetime.time       # Typová anotace pro objekt time

    Typický objekt time:
        - Vytvoření: time(23, 59, 59, 999999, tzinfo=timezone.utc)
        - Z datetime objektu: datetime_obj.time()
        - Z ISO formátu: time.fromisoformat('23:59:59.999999+00:00')
        - Půlnoc: time(0, 0, 0)
        - Aktuální čas: datetime.now().time() (není přímá metoda time.now())

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy datetime.time pomocí isinstance()
        2. Neověřuje vnitřní hodnoty nebo platnost času

    Použití v kódu:
        - Pro parametry funkcí: def schedule_meeting(start_time: time) -> None
        - Pro návratové hodnoty: def get_alarm_time() -> time
        - Pro typování proměnných: lunch_break: time = time(12, 0, 0)

    Specifické informace:
        - Neobsahuje žádné informace o datu na rozdíl od datetime.datetime
        - Lze vytvářet s časovým pásmem (tzinfo) nebo bez něj
        - Podporuje porovnávání, ale pouze mezi objekty time se stejným tzinfo
        - Neměnný (immutable) objekt - po vytvoření nelze měnit jeho hodnoty
        - Nemá přímou podporu pro aritmetické operace (nelze sčítat time objekty)
        - Rozsah hodin je 0-23, minut a sekund 0-59, mikrosekund 0-999999

    Běžné chyby:
        - Záměna datetime.time a datetime.datetime
        - Opomenutí importu `from datetime import time`
        - Porovnávání time objektů s různými časovými pásmy
        - Očekávání date složky v objektu time
        - Pokus o přičítání/odčítání hodnot k/od time objektu (není podporováno)

    Reference:
        - https://docs.python.org/3/library/datetime.html#time-objects
    """

    VALIDATOR_KEY = "time"
    ANNOTATION = time

    IS_INSTANCE = time
    DUCK_TYPING = {
        "has_attr": ("__str__", "isoformat"),
        "has_int_attr": ("hour", "minute", "second", "microsecond")
    }

    DESCRIPTION = "Reprezentace času"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí datetime.time, "
            "tedy reprezentuje denní čas (hodina, minuta, sekunda, mikrosekunda) "
            "bez datové složky a s volitelným časovým pásmem."
        )
