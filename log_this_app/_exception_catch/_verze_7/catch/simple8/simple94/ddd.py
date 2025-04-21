from typing import List, Any, Union

class TypingValidateError(Exception):
    """Chybový oznam pro ověření skrze typing"""
    pass


def tuple_commands(code, value, extras, inner_check):
    return isinstance(value, list)

def list_commands(code, value, extras, inner_check):

    # Validace hodoty
    if isinstance(value, list):

        # Přidání oznamu do extra (pro případné další přístí zpracování)
        extras.append("list")

        # Snížení hodnoty inner_check (Je-li číslem)
        if isinstance(inner_check, int):
            inner_check = max(0, inner_check - 1)

        # Navrácení upravených hodnot
        return value, extras, inner_check

    # Pokud validace neprojde
    else:
        raise TypingValidateError(
            f"Ověření hodnoty selhalo. "
            f"Očekávaný typ: 'list'. Získaný typ: '{type(value)}'"
            f"Ověřovaná hodnota: {value}"
        )


def union_commands(code, value, extras, inner_check):
    for item in value:
        if not validate(code, item, inner_check, extras):
            raise
    return True


# Slovník s příkazy
TYPING_COMMANDS = {
    "tuple": lambda c, v, e, i: tuple_commands(c, v, e, i),
    "list": lambda c, v, e, i: list_commands(c, v, e, i),
    "union": lambda c, v, e, i: union_commands(c, v, e, i),

}


def validate(code, value, extras, inner_check):
    """Rekurzivní metoda pro validaci kodu"""
    command, content = _get_command_and_content(code)

    try:

        # Provedení ověření
        a, b, c = command(content, value, extras, inner_check)
        new_value, new_extras, new_inner_check = a, b, c


        # Pokud je zaplá vnitřní kontrola
        if inner_check and content:

            # Rekurzivní volání pro hlubší úroveň porovnání
            validate(content, new_value, new_inner_check, new_extras)

        # Pokud není zaplá vnitřní kontrola (nebo je vyčerpaná) oznak o úspěšném ověření
        else:
            return True


    # Pokud dojde k vyvolání výjimky (Možná na místo výjimek jen předáváát chybovou zprávu)
    except Exception as e:
        raise TypingValidateError("Vnitřní chyba validace")


def _get_command_and_content(code: List[str]):
    """Metoda pro zpracování kodu a navrácení příkazu a zbylé části"""

    # Zkopírování obsahu code
    content = code[:]

    # Načtení řetězce pro příkaz
    command_str = content.pop(0)

    # Načtení příkazu v slovníku příkazů
    command = TYPING_COMMANDS.get(command_str)

    # Ověření příkazu
    if not command:
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

def parse_typing_annotation(annotation):
    str_annotation = str(annotation).lower()
    expr = str_annotation.replace("typing.", "")
    expr = expr.replace("[", ",[,")
    expr = expr.replace("]", ",],")
    expr = expr.replace(" ", "")
    expr = expr.replace(",,", ",")
    return tuple(expr.strip().lower().split(","))
