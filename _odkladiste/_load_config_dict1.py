from ..utils.read_config_file import read_config_file

class LoadConfigDictMixin:

    def _load_config_dict(self) -> Dict[str, Union[int, str, bool]]:
        """
        Načte konfiguraci ze souboru nebo vytvoří výchozí.

        Returns:
            Dict: Načtená nebo výchozí konfigurace
        """

        # Prvotní nastavení
        config_dict = None
        new_file = True
        broken_file = False

        # Kontrola zda existuje konfigurační soubor
        if self._config_path.exist():

            # Zaznamenání že konfigurační soubor je již vytvořen
            new_file = False

            # Blok zkoušející načtení a validaci dat ze souboru:
            try:
                # Načtení konfiguračního slovníku ze souboru
                config_dict = read_config_file(self.config_path)

                # Kontrola zda jde o slovník s daty
                validate_dict_format(config_dict)

                # Kontrola zda klíče obsahují validní hodnoty
                for key, value in config_dict.items():
                    validate_key_and_value(key, value)

                # Kontrola zda nechybý některé klíče
                if not config_dict_has_all_default_keys(config_dict, self.defaults):

                    # Doplnění chybějícíh klíčů a odstranění přebytečných
                    config_dict = merge_with_defaults(config_dict, self.defaults)

                    # Nastavení vytvoření nového souboru
                    new_file = True

            # Zachycení všech případných výjimek
            except (
                    ReadConfigFileError,
                    ValidateDictFormatError,
                    ValidateKeyAndValueError,
                    ConfigDictHasAllDefaultKeysError,
                    MergeWithDefaultsError,
                    DeleteConfigFileError,
                    SaveConfigFileError
            ) as e:
                # Nastavení vytvoření nového souboru
                config_dict = None
                new_file = True
                self.cli_log.warning(f"{e}", extra=e.extra)

            # Konečná úprava
            finally:

                # Pokud je nastaven pokyn k vytvoření nového souboru
                if new_file:

                    try:
                        # Smazání aktuálního souboru
                        delete_config_file(self.config_path)

                    # Zachycení výjimky při
                    except DeleteConfigFileError as e:
                        # Zaznamenání aby se přeskočilo vytvoření nového souboru
                        new_file = False
                        broken_file = True
                        # Info o tom, že soubor se nepovedlo smazat
                        self.cli_log.warning(f"{e}", extra=e.extra)



        # Pokud je nastaven pokyn k vytvoření nového souboru
        if new_file:

            try:
                # Uložení aktuální konfigurace
                save_config_file(self.config_path, config_dict)

            # Zachycení výjimky pro uložení
            except SaveConfigError as e:
                broken_file = True
                self.cli_log.warning(f"{e}", extra=e.extra)

        # Kontrola zda nedošlo k uložení souboru
        if broken_file:
            # Info o tom, že konfigurace poběží bez možnosti uložit změny do souboru
            self.cli_log.info(f"...", extra={...})


        # Vrácení konfiguračního slovníku
        return config_dict if config_dict else self.defaults
