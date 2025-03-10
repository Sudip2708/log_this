from typing import Tuple

class MultiLineMixin:

    def _handle_multi_line_log(self) -> Tuple[str, str]:
        """
        Určí prázdné řádky pro víceřádkový log.

        Metoda nejprve určí zda předchozí log byl jednořádkový.
        Následně ověří, zda se nejedná o vnitřní volání.
        (V tu chvíli je třeba aby řádkování proběhlo pouze za tímto logem,
        protože předchozí končí na stejné hloubce a tak již mezi nimi prázdný řádek je.)
        Pokud se jedná o vnořené logování, umístí prázdný řádek na začátku i na konci.

        Returns:
            Tuple[str, str]: Start a end prázdné řádky.
        """

        # Pokud předchozí log byl jednořádkový
        if self.thread.last_type == 1:
            return "", "\n"

        # Pokud se nejedná o vnořené volání
        if self.thread.last_depth == self.thread.current_depth:
            return "", "\n"

        # Ve všech ostatních případech
        return "\n", "\n"