from datetime import timedelta

from ..._bases import BaseIsInstanceValidator


class TimedeltaValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci datetime.timedelta

    Typ datetime.timedelta reprezentuje rozdíl (duraci) mezi dvěma daty, časy nebo datetime objekty.
    Uchovává časovou délku jako celkový počet dnů, sekund a mikrosekund.

    Syntaxe:
        - datetime.timedelta       # Vyžaduje import `from datetime import timedelta`

    Příklady použití:
        - datetime.timedelta       # Typová anotace pro objekt timedelta

    Typický objekt timedelta:
        - Vytvoření: timedelta(days=1, hours=2, minutes=30)
        - Z rozdílu: datetime(2023, 1, 2) - datetime(2023, 1, 1)
        - Z počtu sekund: timedelta(seconds=3600)  # 1 hodina
        - Standardní časové intervaly: timedelta(weeks=1), timedelta(days=1)
        - Kombinace: timedelta(days=1, hours=12, minutes=30, seconds=15)

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy datetime.timedelta pomocí isinstance()
        2. Neověřuje vnitřní hodnoty nebo platnost časového intervalu

    Použití v kódu:
        - Pro parametry funkcí: def schedule_reminder(delay: timedelta) -> None
        - Pro návratové hodnoty: def calculate_duration() -> timedelta
        - Pro typování proměnných: timeout: timedelta = timedelta(minutes=5)

    Specifické informace:
        - Podporuje aritmetické operace: sčítání, odčítání, násobení a dělení
        - Lze přičítat a odčítat od datetime objektů: datetime.now() + timedelta(days=1)
        - Lze porovnávat pomocí standardních operátorů (<, >, ==, !=, <=, >=)
        - Interně ukládá tři hodnoty: days, seconds, microseconds
        - Lze mít i záporné hodnoty časového intervalu (pro čas v minulosti)
        - Nemá žádné informace o časových pásmech
        - Nabízí normalizovanou reprezentaci: 0 <= seconds < 86400, 0 <= microseconds < 1000000

    Běžné chyby:
        - Opomenutí importu `from datetime import timedelta`
        - Záměna argumentů při vytváření (weeks, days vs. hours, minutes, seconds)
        - Snaha o přístup k hodinám nebo minutám přímo (timedelta ukládá jen days, seconds, microseconds)
        - Nepochopení normalizované reprezentace (např. 90 minut je uloženo jako 5400 sekund)
        - Snaha odečítat timedelta od prostého čísla

    Reference:
        - https://docs.python.org/3/library/datetime.html#timedelta-objects
    """

    VALIDATOR_KEY = "timedelta"
    ANNOTATION = timedelta

    IS_INSTANCE = timedelta
    HAS_ATTRS = "total_seconds", "__add__", "__sub__", "__str__", "days", "seconds", "microseconds"
    CALLABLE_ATTRS = "days", "seconds", "microseconds"

    DESCRIPTION = "Časový rozdíl mezi dvěma časy"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí datetime.timedelta, tedy reprezentuje rozdíl mezi dvěma časy nebo daty "
            "jako dobu v dnech, sekundách a mikrosekundách."
        )


    LAMBDA = lambda obj: all(
        isinstance(getattr(obj, attr, None), (int, float))
        for attr in ("days", "seconds", "microseconds")
    )