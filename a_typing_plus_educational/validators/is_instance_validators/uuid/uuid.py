from uuid import UUID

from ...._bases import BaseIsInstanceValidator


class UUIDValidator(BaseIsInstanceValidator):
    """
    Validátor pro typovou anotaci uuid.UUID

    Typ uuid.UUID reprezentuje univerzální unikátní identifikátor (UUID) - 128-bitovou
    hodnotu, která je prakticky unikátní napříč časem a prostorem. UUID se běžně používá
    jako identifikátor v distribuovaných systémech, kde je potřeba minimalizovat
    pravděpodobnost kolize identifikátorů.

    Syntaxe:
        - uuid.UUID             # Vyžaduje import `from uuid import UUID`
        - UUID                  # Když je importováno `from uuid import UUID`

    Příklady použití:
        - UUID                  # Typová anotace pro UUID objekt

    Typický objekt UUID:
        - Z řetězce: UUID('12345678-1234-5678-1234-567812345678')
        - Z bajtů: UUID(bytes=b'\x12\x34\x56\x78' * 4)
        - Generování nového UUID: uuid.uuid4() nebo uuid.uuid1()
        - Z polí: UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))

    Validační proces:
        1. Ověří, zda hodnota je instancí třídy uuid.UUID pomocí isinstance()
        2. Neověřuje vnitřní strukturu nebo platnost UUID

    Použití v kódu:
        - Pro parametry funkcí: def get_record(id: UUID) -> Dict
        - Pro návratové hodnoty: def generate_id() -> UUID
        - Pro typování proměnných: record_id: UUID = UUID('12345678-1234-5678-1234-567812345678')

    Specifické informace:
        - Existuje několik verzí UUID (1-5), každá s jiným způsobem generování
        - UUID verzí 4 je generován náhodně a je nejčastěji používaný
        - UUID verzí 1 je generován z MAC adresy a časového razítka
        - Velikost UUID je vždy 128 bitů (16 bajtů)
        - V textové podobě se obvykle zobrazuje jako 32 hexadecimálních číslic s pomlčkami
        - UUID objekt je neměnný (immutable)
        - Lze porovnávat, řadit a používat jako klíč ve slovníku

    Běžné chyby:
        - Opomenutí importu `from uuid import UUID`
        - Záměna řetězcové reprezentace UUID a UUID objektu
        - Nesprávný formát řetězce při vytváření UUID
        - Záměna různých verzí UUID (uuid1, uuid4) a jejich vlastností
        - Předpoklad absolutní unikátnosti (teoreticky může dojít ke kolizi, i když je pravděpodobnost extrémně nízká)

    Reference:
        - https://docs.python.org/3/library/uuid.html
        - https://tools.ietf.org/html/rfc4122 (A Universally Unique IDentifier (UUID) URN Namespace)
    """

    VALIDATOR_KEY = "UUID"
    ANNOTATION = UUID

    IS_INSTANCE = UUID
    DUCK_TYPING = {
        "has_attr": ("hex", "int", "urn", "bytes"),
    }

    DESCRIPTION = "Univerzální unikátní identifikátor"
    LONG_DESCRIPTION = (
            "Validuje, že objekt je instancí uuid.UUID, "
            "tedy univerzálním unikátním identifikátorem, který poskytuje "
            "128-bitovou hodnotu pro jednoznačnou identifikaci napříč systémy."
        )

