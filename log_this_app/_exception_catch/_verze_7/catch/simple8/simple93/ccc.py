from typing import List, Any, Union

class TypingValidateError(Exception):
    pass

class TypingCheck:

    # Slovník s příkazy
    commands = {
        tuple: lambda:value, extras, inner_check self.tuple,

    }


    def __call__(
            self,
            code: List[str],
            value: Any,
            inner_check: Union[bool, int] = True
    ):
        self._code = code
        self._value = value
        self._inner = inner_check

        return self.validate()


    def validate(self, code, value, inner_check, extras):
        """Rekurzivní metoda pro validaci kodu"""
        command, content = self._get_command_and_content(code)

        try:

            # Provedení ověření
            a, b, c = command(value, extras, inner_check)
            new_value, new_extras, new_inner_check = a, b, c

            # Ověření zda prošlo (podle hodnoty new_extras - True, False, str)
            if new_extras:

                # Pokud je zaplá vnitřní kontrola
                if inner_check and content:

                    # Rekurzivní volání pro hlubší úroveň porovnání
                    self.validate(content, new_value, new_inner_check, new_extras)

                # Pokud není zaplá vnitřní kontrola (nebo je vyčerpaná) oznak o úspěšném ověření
                else:
                    return True

            # Pokudje výsledek ověření negativní
            else:

                # Vyvolání výjimky (možná vracet jen oznam a pak ho skládat)
                raise TypingValidateError(command(value, message=True))

        # Pokud dojde k vyvolání výjimky
        except Exception as e:
            raise TypingValidateError("Vnitřní chyba validace")


    def _get_command_and_content(self, code: List[str]):
        """Metoda pro zpracování kodu a navrácení příkazu a zbylé části"""

        # Zkopírování obsahu code
        content = code[:]

        # Načtení řetězce pro příkaz
        command_str = content.pop(0)

        # Načtení příkazu v slovníku příkazů
        command = self.commands.get(command_str)

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


