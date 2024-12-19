from typing import Tuple


class BlankLinesHandler:
    """
    Zpracovává logiku pro vkládání prázdných řádků v logování.

    Attributes:
        config (dict): Konfigurace nastavení prázdných řádků.
        thread_context (ThreadContext): Kontext aktuálního vlákna.
    """

    def __init__(self, config, thread_context):
        """
        Inicializuje handler pro prázdné řádky.

        Args:
            config (dict): Konfigurace nastavení.
            thread_context (ThreadContext): Kontext vlákna.
        """

        self.config = config
        self.thread_context = thread_context


    def get_blank_lines(self) -> Tuple[str, str]:
        """
        Určí prázdné řádky podle kontextu logování.

        Returns:
            Tuple[str, str]: Start a end prázdné řádky.
        """

        # Pokud nejsou prázdné řádky požadované
        if not self.config.blank_lines:
            return "", ""

        # Pokud se jedná o jednořádkový výpis
        if self.thread_context.thread.current_type == 1:
            start_blank, end_blank = self._handle_one_line_log()

        # Pokud se jedná o víceřádkový výpis
        else:
            start_blank, end_blank = self._handle_multi_line_log()

        return start_blank, end_blank

    def _handle_one_line_log(self) -> Tuple[str, str]:
        """
        Určí prázdné řádky pro jednořádkový log.

        Returns:
            Tuple[str, str]: Start a end prázdné řádky.
        """

        # Načtení hodnoty
        thread = self.thread_context.thread

        if thread.last_type == 1:
            return "", "\n"

        if thread.last_depth < thread.current_depth:
            return "\n", "\n"

        return "", "\n"

    def _handle_multi_line_log(self) -> Tuple[str, str]:
        """
        Určí prázdné řádky pro víceřádkový log.

        Returns:
            Tuple[str, str]: Start a end prázdné řádky.
        """
        thread = self.thread_context.thread

        if thread.last_depth == thread.current_depth:
            return "", "\n"

        if thread.last_type == 1:
            return "", "\n"

        return "\n", "\n"