class DecreaseDepthMixin:


    def decrease_depth(self):
        """
        Sníží hodnotu hloubky zanoření.

        Notes:
            Sníží hloubku zanoření a uloží poslední dosaženou hloubku.
        """

        # Přepis minulé hloubky na hodnotu která reprezentovala současný stav
        self.thread.last_depth = self.thread.current_depth

        # Přepis hodnoty reprezentující současný stav na aktuální hodnotu
        self.thread.current_depth -= 1
