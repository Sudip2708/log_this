from threading import local


class ThreadContext:
    """
    Spravuje kontextové informace pro jednotlivá vlákna během logování.

    Attributes:
        thread (threading.local): Lokální úložiště pro každé vlákno.
    """

    def __init__(self):
        """Inicializuje lokální úložiště pro vlákno."""
        self.thread = local()

    def initialize_state(self):
        """
        Inicializuje výchozí stav pro aktuální vlákno.

        Notes:
            Nastaví počáteční hodnoty pro hloubku, typ a historii volání.
        """
        if not hasattr(self.thread, "current_depth"):
            self.thread.current_depth = 0
            self.thread.last_depth = 0
            self.thread.current_type = 0
            self.thread.last_type = 0

    def update_context(self, mode: int):
        """
        Aktualizuje kontext logování pro aktuální vlákno.

        Args:
            mode (int): Aktuální typ logování.

        Notes:
            - Inicializuje stav vlákna, pokud dosud nebyl
            - Zvyšuje hloubku zanoření
            - Ukládá informace o předchozím a aktuálním typu
        """
        if not hasattr(self.thread, "current_depth"):
            self.initialize_state()
        else:
            self.thread.current_depth += 1

        self.thread.last_type = self.thread.current_type
        self.thread.current_type = mode

    def revert_context(self):
        """
        Upraví kontext po dokončení logování.

        Notes:
            Sníží hloubku zanoření a uloží poslední dosaženou hloubku.
        """
        self.thread.last_depth = self.thread.current_depth
        self.thread.current_depth -= 1
