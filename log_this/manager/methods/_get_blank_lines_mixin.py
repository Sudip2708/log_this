from typing import Tuple
from .blank_lines_mixins import OneLineMixin, MultiLineMixin

class GetBlankLinesMethodsMixins(OneLineMixin, MultiLineMixin):

    def get_blank_lines(self) -> Tuple[str, str]:
        """
        Určí prázdné řádky podle kontextu logování.

        Metoda nejprve zjistí jaká je hodnota pro řádkování v konfiguračním souboru.
        Pokud je hodnota False, vrátí řetězec bez odskoku na další řádku.
        Pokud je hodnota True, ověří, zda předchozí log byl jednořádkový
        (a neměl možnost pro vnitřní volání), nebo zda byl víceřádkový
        (a měl možnost pro vnitřní volání), a volá metodu pro spracování,
        a navrácení řádkovaní dle porovnání modu a hloubky zanoření.

        Returns:
            Tuple[str, str]: Start a end prázdné řádky.
        """

        # Pokud nejsou prázdné řádky požadované
        if not self.config["blank_lines"]:
            return "", ""

        # Pokud se jedná o jednořádkový výpis
        if self.thread.current_type == 1:
            return self._handle_one_line_log()

        # Pokud se jedná o víceřádkový výpis
        else:
            return self._handle_multi_line_log()




