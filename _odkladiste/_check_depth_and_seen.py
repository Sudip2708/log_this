from typing import Any, Optional

class CheckDepthAndSeenMixin:

    def check_depth_and_seen(
            self,
            obj: Any,
            depth: int
    ) -> Optional[str]:
        """
        Metoda pro kontrolu rekurze a cyklických referencí.

        Tato metoda provádí dvě kontroly:
        1. Ověří, zda aktuální hloubka rekurze nepřekračuje maximální povolenou hodnotu (`max_depth`).
        2. Zkontroluje, zda ID objektu není již v množině viděných objektů (`seen`), čímž detekuje cyklické reference.

        Pokud některá z těchto podmínek selže, metoda vrátí chybovou zprávu.
        Pokud obě kontroly projdou, přidá ID objektu do množiny viděných objektů a umožní pokračování v serializaci.

        Parametry:
            obj (Any): Objekt, který je kontrolován. Tento parametr by měl být jakýkoliv objekt, u kterého se
                       kontroluje rekurze a cyklické reference. Například instance tříd nebo jiných datových struktur.
            depth (int): Aktuální hloubka rekurze. Tento parametr udává úroveň vnoření aktuálně zpracovávaného objektu.

        Return:
            Optional[str]: Pokud je dosažena maximální hloubka rekurze nebo je detekována cyklická reference,
                            metoda vrátí chybovou zprávu ve formě řetězce. Pokud kontrola projde bez problémů, vrací `None`.

        Výjimky:
            Žádné výjimky nejsou vyvolány, ale vrácený řetězec obsahuje chybové zprávy při porušení podmínek.
        """

        print("### def check_depth_and_seen: ")
        # Kontrola maximální hloubky rekurze
        if depth >= self.max_depth:
            print("### if depth >= self.max_depth: ", obj)
            return "<SerializationError: Maximum serialization depth exceeded>"

        # Kontrola přímé rekurze (objekty mají shodné ID)
        if id(obj) in self.seen:
            print("### if id(obj) in self.seen: ", obj)
            return "<SerializationError: Cyclic reference detected>"

        # Přidání ID objektu do `seen`
        self.seen.add(id(obj))
        print("### def check_depth_and_seen: ", obj)
        return True
