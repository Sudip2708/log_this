from typing import Union


class SetNewValueMixin:

    def set_new_value(
            self,
            key: str,
            value: Union[int, str, bool]
    ) -> None:
        """
        Aktualizuje hodnotu konfigurace a uloží ji.

        Metoda nejprve zkontroluje přítomnos klíče v defaultním slovníku,
        a ověří platnost hodnoty.
        Následně metoda změní hodnotu pro daný klíč v instanční konfiguraci.
        Nakonec metoda uloží hodnoty do konfiguračního souboru.
        Pokud se to nepovede, metoda načte zpět původní hodnoty.

        Args:
            key (str): Klíč konfigurace pro aktualizaci
            value (Union[int, str, bool]): Nová hodnota konfigurace

        Raises:
            KeyError: Při pokusu o aktualizaci neexistujícího klíče
            ValueError: Při pokusu o nastavení neplatné hodnoty
        """


        # Kontrola klíče a hodnoty
        try:
            self._validate_key_and_value(key, value)
        # Zachycení špatného klíče a hodnoty
        except (KeyError, ValueError) as e:
            self.cli_log.error(e, extra=e.extra if e.extra else None)



        # Kontrola, zda již hodnota nebyla aktualizovaná
        if self.config[key] == value:
            self.cli_log.info("No Change Needed",
                extra = {
                    "detail": f"The configuration key '{key}' is already set to '{value}'",
                    "help": "Pokud cheš vidět aktuální konfiguraci: $ log-this-config --show \n"
                            "Pro podrobnější nápovědu: $ log-this-config --help "
                }
            )
            return



        # Uložení změny do instance třídy
        self.config[key] = value
        self.cli_log.success("The configuration was changed",
            extra = {
                "detail": f"The key '{key}' has been set to '{value}'",
            }
        )

        # Uložení změny do konfiguračního souboru
        try:
            self._create_config_file(self.config):
        except (KeyError, ValueError) as e:
            self.cli_log.info(e, extra=e.extra if e.extra else {})


        # Dodatečná úprava pro nastavení maximální rekurze pro serializer
        if key == "max_depth":
            try:
                self.update_max_depth_in_serealizer(value)
            except (KeyError, ValueError) as e:
                self.cli_log.info(e, extra=e.extra if e.extra else {})


    def update_max_depth_in_serealizer(self, value):
        try:
            from log_this.manager.serializer import get_serializer
            serializer = get_serializer()
            serializer.max_depth = value
        except (KeyError, ValueError) as e:
            self.cli_log.info(e, extra=e.extra if e.extra else {})




        # Kontrola klíče a hodnoty
        if self._validate_key_and_value(key, value):

            # Uložení změny do instance třídy
            self.config[key] = value
            self.cli_log.success("Configuration Updated",
                extra = {
                    "detail": f"The configuration for the key '{key}' has been set to '{value}'",
                    "help": "Pokud cheš vidět aktuální konfiguraci: $ log-this-config --show \n"
                          "Pro podrobnější nápovědu: $ log-this-config --help "
                }
            )

            # Uložení změny do konfiguračního souboru
            if not self._create_config_file(self.config):
                self.cli_log.success(
                    f"The new configuration has been saved to a file: "
                )

            # Pokud uložení změny neproběhlo v pořádku
            else:
                self.file_log.error(
                    f"Error while update config: "
                    f"The configuration file could not be updated. \n"
                    f"Running info for this Error: "
                    f"The library will run without a configuration file. \n"
                    f"Possible limitations: "
                    f"Default values will be loaded, which can be changed, "
                    f"but they will not be saved for next time."
                )

            # Dodatečná úprava pro nastavení maximální rekurze pro serializer
            if key == "max_depth":
                from log_this.manager.serializer import get_serializer
                serializer = get_serializer()
                serializer.max_depth = value
                self.file_log.info(
                    f"Success with update config file: "
                    f"The SafeSerializer class attribute 'max_depth' "
                    f"was changed to {value} "
                )

        # Pokud validace neproběhne úspěšně
        else:
            self.file_log.error(
                f"Error while update config: "
                f"Could not update key {key} to value {value}. "
                f"The values provided are not valid."
            )

