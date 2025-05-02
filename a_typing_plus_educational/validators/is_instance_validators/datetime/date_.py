from datetime import date

from ..._bases import BaseIsInstanceValidator


class DateValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci datetime.date

    Typ datetime.date reprezentuje kalendářní datum (rok, měsíc a den)
    bez časové složky a bez informace o časovém pásmu.

    Syntaxe:
        - datetime.date       # Vyžaduje import `from datetime import date`

    Příklady použití:
        - datetime.date       # Typová anotace pro objekt date

    Typický objekt date:
        - Vytvoření: date(2023, 12, 31)
        - Dnešní datum: date.today()
        - Z datetime objektu: datetime_obj.date()
        - Z ISO formátu: date.fromisoformat('2023-12-31')
        - Z časového razítka: date.fromtimestamp(1672444800)

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy datetime.date pomocí isinstance()
        2. Neověřuje vnitřní hodnoty nebo platnost data

    Použití v kódu:
        - Pro parametry funkcí: def process_event(event_date: date) -> None
        - Pro návratové hodnoty: def get_birthday() -> date
        - Pro typování proměnných: deadline: date = date(2023, 12, 31)

    Specifické informace:
        - Neobsahuje žádné informace o čase na rozdíl od datetime.datetime
        - Podporuje základní operace jako porovnávání, výpočet rozdílu dnů
        - Rozdíl dvou date objektů vrací datetime.timedelta
        - Neměnný (immutable) objekt - po vytvoření nelze měnit jeho hodnoty
        - Interval je mezi lety 1 až 9999

    Běžné chyby:
        - Záměna datetime.date a datetime.datetime
        - Opomenutí importu `from datetime import date`
        - Pokus o získání časových informací z date objektu
        - Záměna pořadí argumentů při vytváření (rok, měsíc, den vs. den, měsíc, rok)
        - Pokus o vytvoření neplatného data (například 31. února)

    Reference:
        - https://docs.python.org/3/library/datetime.html#date-objects
    """

    VALIDATOR_KEY = "date"
    ANNOTATION = date

    IS_INSTANCE = date
    HAS_ATTRS = "isoformat", "weekday", "__str__", "year", "month", "day"
    CALLABLE_ATTRS = "year", "month", "day"

    DESCRIPTION = "Reprezentace data"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí datetime.date, "
            "tedy reprezentuje kalendářní datum (rok, měsíc, den) "
            "bez časové složky a časového pásma."
        )


    LAMBDA = lambda obj: all(
        isinstance(getattr(obj, attr, None), int) for attr in
        ("year", "month", "day"))
