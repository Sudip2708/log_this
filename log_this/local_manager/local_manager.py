from log_this.config import get_config
from ._thread_context import ThreadContext
from ._indent_handler import IndentHandler
from ._blank_lines_handler import BlankLinesHandler


class LocalManager:
    """
    Centrální správce pro lokální kontext logování.

    Spravuje komplexní logiku určování prázdných řádků a odsazení
    podle kontextu volání a typu logování.

    Attributes:
        config (dict): Konfigurace nastavení logování.
        thread_context (ThreadContext): Kontext pro aktuální vlákno.
        indent_handler (IndentHandler): Handler pro zpracování odsazení.
        blank_lines_handler (BlankLinesHandler): Handler pro prázdné řádky.
    """

    def __init__(self):
        """
        Inicializuje LocalManager s načtením konfigurace a nastavením kontextu.
        """
        self.config = get_config()
        self.thread_context = ThreadContext()
        self.indent_handler = IndentHandler(self.config, self.thread_context)
        self.blank_lines_handler = BlankLinesHandler(self.config,
                                                     self.thread_context)

    def update_context(self, mode: int):
        """
        Deleguje aktualizaci kontextu na ThreadContext.

        Args:
            mode (int): Typ aktuálního logování.
        """
        self.thread_context.update_context(mode)

    def revert_context(self):
        """Vrátí kontext do předchozího stavu."""
        self.thread_context.revert_context()

    def get_indent(self) -> str:
        """
        Získá řetězec pro odsazení.

        Returns:
            str: Řetězec pro odsazení.
        """
        return self.indent_handler.get_indent()

    def get_blank_lines(self) -> tuple:
        """
        Získá prázdné řádky pro aktuální kontext.

        Returns:
            tuple: Start a end prázdné řádky.
        """
        return self.blank_lines_handler.get_blank_lines()
