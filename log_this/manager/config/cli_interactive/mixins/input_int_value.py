def _input_int_value(self) -> Optional[Any]:



    while True:

        # Vytvoření inputu
        result = input_dialog(
            title=f'Zadejte celočíselnou hodnotu:',
            style=self.style
        ).run()

        # Pokud uživatel zruší dialog
        if not result:
            return None

        # Pokus o převod hodnoty
        value = self._convert_value(result)

        # Kontrola, zda nebyla zadaná již existující hodnota
        if value == current_value:
            print(
                f"\nThe configuration key '{key}' is already set to '{value}'. \n"
                f"Žádná změna nebyla učiněna. \n")
            return None

        # Validace hodnoty
        if key_data.validate(value):
            return value
        else:
            print(f"\nNeplatná hodnota: '{result}'. Zkuste to znovu.\n")
