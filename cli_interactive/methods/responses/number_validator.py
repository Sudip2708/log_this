from prompt_toolkit.validation import Validator, ValidationError

class NumberValidator(Validator):

    text = None
    error_message = ' ⚠ Neplatná hodnota! Zadej celé číslo v rozmezí 0 - 1000 '

    def raise_validation_error(self):
        """Metoda pro vyvolání výjimky"""
        raise ValidationError(
            message=self.error_message,
            cursor_position=len(self.text),
        )

    def validate(self, document):
        """Metoda pro kontrolu vstupu"""

        # Přidání vstupní hodnoty do atributu
        self.text = document.text

        # Pokud je nějaký text (prázdný pole je povolené pro návrat)
        if self.text:

            # Kontrola zda je to číslo
            if not self.text.isdigit():
                self.raise_validation_error()

            # Kontrola zda nezačíná nulou
            if len(self.text) > 1 and self.text[0] == '0':
                self.raise_validation_error()

            # Kontrola rozsahu
            if not (0 <= int(self.text) <= 1000):
                self.raise_validation_error()


