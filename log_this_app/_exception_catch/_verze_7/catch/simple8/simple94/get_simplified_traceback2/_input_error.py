class GetSimplifiedTracebackInputError(TypeError):
    """Výjimka pro kontrolu vstupních hodnot třídy GetSimplifiedTraceback."""

    title = "Zadán neplatný vstupní parametr pro GetSimplifiedTraceback. \n"

    def __init__(
            self,
            parameter: str,
            input_value: any,
            allowed_value: str,
            description: str
    ):
        """
        Inicializace výjimky pro kontrolu vstupních hodnot.

        Args:
            parameter: Název parametru, který způsobil výjimku
            input_value: Hodnota, která byla zadána
            allowed_value: Popis povolených hodnot
            description: Popis účelu parametru
        """
        self.parameter = parameter
        self.input_value = input_value
        self.allowed_value = allowed_value
        self.description = description
        self.message = (
                self.title
                + f"Vstupní parametr '{self.parameter}' \n"
                + f"Zadaná hodnota: {self.input_value} \n"
                + f"Povolené hodnoty: {self.allowed_value} \n"
                + f"Popis parametru: {self.description} \n"
        )
        super().__init__(self.message)

    def __str__(self) -> str:
        """Vrátí textovou reprezentaci výjimky."""
        return self.message
