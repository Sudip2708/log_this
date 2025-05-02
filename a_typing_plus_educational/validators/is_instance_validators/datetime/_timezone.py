from datetime import timezone

from ..._bases import BaseIsInstanceValidator


class TimezoneValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci datetime.timezone

    Typ datetime.timezone reprezentuje fixní offset od UTC (Coordinated Universal Time).
    Je konkrétní implementací abstraktní třídy datetime.tzinfo.

    Syntaxe:
        - datetime.timezone       # Vyžaduje import `from datetime import timezone`

    Příklady použití:
        - datetime.timezone       # Typová anotace pro objekt timezone

    Typický objekt timezone:
        - UTC: timezone.utc
        - S offsetem: timezone(timedelta(hours=2))  # UTC+2
        - Z offsetu v sekundách: timezone(timedelta(seconds=7200))  # Také UTC+2

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy datetime.timezone pomocí isinstance()
        2. Neověřuje vnitřní hodnoty nebo platnost časového pásma

    Použití v kódu:
        - Pro parametry funkcí: def format_time(tz: timezone) -> str
        - Pro návratové hodnoty: def get_local_timezone() -> timezone
        - Pro typování proměnných: local_tz: timezone = timezone(timedelta(hours=1))

    Specifické informace:
        - Je konkrétní implementací abstraktní třídy datetime.tzinfo
        - Reprezentuje fixní offset od UTC (nemění se se změnami letního času)
        - Pro dynamická časová pásma (např. s letním časem) je třeba použít jiné knihovny
        - timezone.utc je předdefinovaná konstanta reprezentující UTC (offset 0)
        - Neměnný (immutable) objekt - po vytvoření nelze měnit jeho hodnoty

    Běžné chyby:
        - Opomenutí importu `from datetime import timezone`
        - Záměna timezone a tzinfo (timezone je implementace tzinfo)
        - Použití pro dynamická časová pásma (se změnami pro letní čas)
        - Vytváření timezone bez timedelta: timezone(hours=2) místo timezone(timedelta(hours=2))

    Reference:
        - https://docs.python.org/3/library/datetime.html#timezone-objects
    """

    VALIDATOR_KEY = "timezone"
    ANNOTATION = timezone

    IS_INSTANCE = timezone
    HAS_ATTRS = "utcoffset", "tzname", "__str__"
    CALLABLE_ATTRS = "utcoffset", "tzname"

    DESCRIPTION = "Časové pásmo s pevným posunem"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí datetime.timezone, "
            "tedy reprezentuje časové pásmo jako pevný posun "
            "od UTC (Coordinated Universal Time)."
        )


    LAMBDA = lambda obj: (
            callable(getattr(obj, "utcoffset", None))
            and callable(getattr(obj, "tzname", None))
    )
