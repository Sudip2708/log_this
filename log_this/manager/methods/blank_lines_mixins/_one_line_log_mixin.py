from typing import Tuple

class OneLineMixin:

    def _handle_one_line_log(self) -> Tuple[str, str]:
        """
        Určí prázdné řádky pro jednořádkový log.

        Metoda nejprve určí zda předchozí log byl jednořádkový.
        Následně ověří, zda se jedná o vnitřní volání.
        (V tu chvíli je třeba aby řádkování proběhlo před i za tímto logem.)

        Returns:
            Tuple[str, str]: Start a end prázdné řádky.
        """

        # Pokud předchozí log byl jednořádkový
        if self.thread.last_type == 1:
            return "", "\n"

        # Pokud se jedná o vnořené volání
        if self.thread.last_depth < self.thread.current_depth:
            return "\n", "\n"

        # Ve všech ostatních případech
        return "", "\n"