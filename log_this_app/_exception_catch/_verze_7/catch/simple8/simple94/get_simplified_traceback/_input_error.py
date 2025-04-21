

class GetSimplifiedTracebackInputError(TypeError):
    """Víjimka pro kontolu vstupních hodnot třídy GetSimplifiedTraceback"""

    title = "Zadán neplatný vstupní parametr pro GetSimplifiedTraceback. \n"

    def __init__(
            self,
            parameter: str,
            input_value: str,
            allowed_value: str,
            description: str
    ):
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

    def __str__(self):
        return self.message
