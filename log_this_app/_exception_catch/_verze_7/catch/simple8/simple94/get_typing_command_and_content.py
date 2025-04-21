from typing import List

from .typing_validate_error import TypingValidateError
from .typing_commands import TYPING_COMMANDS


def get_typing_command_and_content(code: List[str]):
    """Metoda pro zpracování kodu a navrácení příkazu a zbylé části"""

    # Zkopírování obsahu code
    content = code[:]

    # Načtení řetězce pro příkaz
    command_str = content.pop(0)

    # Načtení příkazu v slovníku příkazů
    command = TYPING_COMMANDS.get(command_str)

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
