from typing import List

from .typing_validate_error import TypingValidateError
from .typing_commands import TYPING_COMMANDS

class GetTypingCommandAndContentMixin(ABC):

    def get_typing_command_and_content(self):
        """Metoda pro zpracování kodu a navrácení příkazu a zbylé části"""

        # Převod typing anotace na seznam řetězců
        typing_code = self._get_typing_code()

        # Načtení řetězce pro příkaz
        command_str = typing_code.pop(0)

        # Načtení příkazu v slovníku příkazů
        command = self.TYPING_COMMANDS.get(command_str)

        # Ověření příkazu
        if not command:

            # Kontrola zda se jedná o běžný typ
            if isinstance(command, type):
                return
            raise TypingValidateError(
                f"Nepovedlo se rozpoznat příkaz: {command_str}"
            )

        # Pokud již není další obsah
        if not content:

            # Navrácení hodnot
            return command, content

        # Pokud je ještě další obsah
        else:

            # Načtení dalšího příkazu
            start = content.pop(0)

            # Ověření, jestli je další příkaz závorka
            if start == "[":

                # Načtení posledního příkazu
                end = content.pop()

                # Ověření, jestli je poslení znak také závorka
                if end == "]":

                    # Navrácení hodnot
                    return command, content

                # Pokud koncová závorka chybí
                else:
                    raise TypingValidateError(
                        f"V zápisu chybý koncová hranatá závorka: {code}"
                    )

            # Pokud úvodní závorka chybí
            else:
                raise TypingValidateError(
                    f"V zápisu chybý úvodní hranatá závorka: {code}"
                )
