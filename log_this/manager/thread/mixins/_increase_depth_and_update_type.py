class IncreaseDepthAndUpdateTypeMixin:


    def increase_depth_and_update_type(self, mode: int):
        """
        Aktualizuje kontext logování pro aktuální vlákno.

        Args:
            mode (int): Aktuální typ logování.

        Notes:
            - Inicializuje stav vlákna, pokud dosud nebyl
            - Zvyšuje hloubku zanoření
            - Ukládá informace o předchozím a aktuálním typu
        """

        # Pokud ano, dojde k přípočtu hloubky
        self.thread.current_depth += 1

        # Přepis minulého modu na hodnotu která reprezentovala současný mod
        self.thread.last_type = self.thread.current_type

        # Přepis hodnoty reprezentující současný mod na aktuální hodnotu
        self.thread.current_type = mode

