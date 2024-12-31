class IndentHandler:
    """
    Zpracovává logiku odsazení pro logovací záznamy.

    Attributes:
        config (dict): Konfigurace nastavení odsazení.
        thread_context (ThreadContext): Kontext aktuálního vlákna.
    """

    def __init__(self, config, thread_context):
        """
        Inicializuje handler pro odsazení.

        Args:
            config (dict): Konfigurace nastavení.
            thread_context (ThreadContext): Kontext vlákna.
        """
        self.config = config
        self.thread_context = thread_context

    def get_indent(self) -> str:
        """
        Vygeneruje odsazení podle aktuální hloubky volání.

        Returns:
            str: Řetězec pro odsazení, nebo prázdný řetězec.
        """
        if not self.config.indent:
            return ""

        return " " * self.config.indent * self.thread_context.thread.current_depth