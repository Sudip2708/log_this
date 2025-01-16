from ..utils.read_config_file import read_config_file

class LoadConfigDictMixin:

    def _load_config_dict(self) -> Dict[str, Union[int, str, bool]]:
        """
        Načte konfiguraci ze souboru nebo vytvoří výchozí.

        Returns:
            Dict: Načtená nebo výchozí konfigurace
        """

        # Kontrola zda existuje konfigurační soubor
            # Pokud ano, kontrola, zda se z něj dají načíst data
                # Pokud ano, kontrola zda jsou data validní
                    # Pokud ano, předat je jako konfigurační slovník
                    # Pokud ne, předat jako konfigurační slovník @property default
                        # Pokusit se uložit default do souboru
                            # Pokud vše proběhne v pořádku nevypisovat nic
                            # Pokud se nepovede vytvořit konfigurační soubor, informativní log - né výjimka
                # Pokud ne ...
            # Pokud ne ...
        # Pokud ne ...

        # Kontrola zda existuje konfigurační soubor
        if self._config_path.exist():

            # Blok zkoušející zda validace souboru proběhne v pořádku:
            try:

                # Načtení konfiguračního slovníku ze souboru
                try:
                    config_data = read_config_file(self.config_path)
                except ReadConfigFileError as e:
                    self.cli_log.warning(f"{e}", extra=e.extra)
                    raise


                # Kontrola zda jde o slovník s daty
                try:
                    config_dict = validate_config_format(config_data)
                except ValidateConfigFormatError as e:
                    self.cli_log.warning(f"{e}", extra=e.extra)
                    raise


                # Kontrola klíčů a hodnot
                try:
                    for key, value in config_dict.items():
                        validate_key_and_value(key, value)
                except ValidateKeyAndValueError as e:
                    self.cli_log.warning(f"{e}", extra=e.extra)
                    raise

                # Kontrola zda jsou v slovníku všechny klíče
                # Pokud ne, dopsat ty co tam nejsou s defaultními hodnotami


                # Pokud vše proběhne v pořádku navrátit ověřená data
                return config_dict


            # Možná nastavit logování o neúspěchu až sem a v kodu výše jen předat výjimku?
            except (ReadConfigFileError, ValidateConfigFormatError, ValidateKeyAndValueError) as e:
                self.cli_log.warning(f"{e}", extra=e.extra)
                # Nastavit atribut pro vytvoření slovníku.
                # Pokud validace projdou a jen nebudou uvedené všechny klíče, tak doplnit



            # Možná udělat z celého honího bloku metodu, či funkci a zde mít jen try/except blok
            # A nebo zkrátit zápis na
            # Blok zkoušející zda validace souboru proběhne v pořádku:
            try:
                # Načtení konfiguračního slovníku ze souboru
                config_dict = read_config_file(self.config_path)

                # Kontrola zda jde o slovník s daty
                validate_dict_format(config_dict)

                # Kontrola klíčů a hodnot
                for key, value in config_dict.items():
                    validate_key_and_value(key, value)

                # Kontrola zda jsou v slovníku všechny klíče

                # Pokud ne, dopsat ty co tam nejsou s defaultními hodnotami

                # Pokud vše proběhne v pořádku navrátit ověřená data
                return config_dict

            except (ReadConfigFileError, ValidateConfigFormatError, ValidateKeyAndValueError) as e:
                self.cli_log.warning(f"{e}", extra=e.extra)



        # Pokud slovník ještě není vytvořen a nebo se nepovedlo načíst
        # Vrátit defaultní data
        # Pokusit se uložit slovník
        return self.defaults


