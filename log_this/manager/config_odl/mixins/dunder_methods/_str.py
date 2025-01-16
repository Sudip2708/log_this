class StrMixin:

    def __str__(self) -> str:
        """
        Vrací čitelnou reprezentaci konfigurace ve formě řetězce.

        Metoda používá join namísto konkatenaci, protože je nejenom
        více idiomatická, ale i šetrnější na prostředky.

        Returns:
            str: Formátovaný výpis aktuální konfigurace.
        """

        formatted_config = "\n".join(
            f"{key}: {value}" for key, value in self.config.items())
        return f"LogThisConfig:\n{formatted_config}"

