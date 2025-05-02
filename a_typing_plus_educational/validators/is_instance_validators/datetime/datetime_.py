from datetime import datetime

from ..._bases import BaseIsInstanceValidator


class DatetimeValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci datetime.datetime

    Typ datetime.datetime reprezentuje konkrétní datum a čas s přesností až na mikrosekundy.
    Obsahuje informace o roce, měsíci, dni, hodině, minutě, sekundě, mikrosekundě
    a může zahrnovat i informaci o časovém pásmu.

    Syntaxe:
        - datetime.datetime       # Vyžaduje import `from datetime import datetime`

    Příklady použití:
        - datetime.datetime       # Typová anotace pro objekt datetime

    Typický objekt datetime:
        - Vytvoření: datetime(2023, 12, 31, 23, 59, 59, 999999, tzinfo=timezone.utc)
        - Aktuální datum a čas: datetime.now() nebo datetime.utcnow()
        - Analýza řetězce: datetime.fromisoformat('2023-12-31T23:59:59+00:00')
        - Časové razítko: datetime.fromtimestamp(1672527599.999999)

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy datetime.datetime pomocí isinstance()
        2. Neověřuje vnitřní hodnoty nebo platnost datetime objektu

    Použití v kódu:
        - Pro parametry funkcí: def process_event(event_time: datetime) -> None
        - Pro návratové hodnoty: def get_creation_time() -> datetime
        - Pro typování proměnných: event_start: datetime = datetime.now()

    Specifické informace:
        - Na rozdíl od datetime.date obsahuje i informaci o čase
        - Na rozdíl od datetime.time obsahuje i informaci o datu
        - Podporuje operace jako porovnávání, rozdíl (výsledkem je timedelta)
        - Může být timezone-aware (s časovým pásmem) nebo timezone-naive (bez časového pásma)
        - Neměnný (immutable) objekt - po vytvoření nelze měnit jeho hodnoty

    Běžné chyby:
        - Záměna datetime.datetime a datetime.date
        - Opomenutí importu `from datetime import datetime`
        - Porovnávání timezone-aware a timezone-naive datetime objektů
        - Chybné převody mezi časovými pásmy
        - Zaměnění pořadí argumentů při vytváření (rok, měsíc, den vs. den, měsíc, rok)

    Reference:
        - https://docs.python.org/3/library/datetime.html#datetime-objects
    """

    VALIDATOR_KEY = "datetime"
    ANNOTATION = datetime

    IS_INSTANCE = datetime
    HAS_ATTRS = "isoformat", "timestamp", "__str__", "year", "month", "day", "hour", "minute", "second", "microsecond"
    CALLABLE_ATTRS = "year", "month", "day", "hour", "minute", "second", "microsecond"

    DESCRIPTION = "Reprezentace data a času"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí datetime.datetime, "
            "tedy reprezentuje kombinaci data a času "
            "s volitelným časovým pásmem."
        )


    LAMBDA = lambda obj: all(
        isinstance(getattr(obj, attr, None), int)
        for attr in
        ("year", "month", "day", "hour", "minute", "second", "microsecond")
    )