class LoadConfigDictMixin:

    def _load_config_dict(self) -> Dict[str, Union[int, str, bool]]:
        """
        Načte konfiguraci ze souboru nebo vytvoří výchozí.

        Returns:
            Dict: Načtená nebo výchozí konfigurace
        """
        try:
            # Pokus o načtení konfigurace
            with self._config_path.open('r') as f:
                config = json.load(f)

            # Validace načtené konfigurace
            if self._validate_config_dict(config):
                return config

        except (json.JSONDecodeError, FileNotFoundError, ValueError) as e:
            self.cli_log.warning(
                f"Nepodařilo se načíst konfigurační soubor ({str(e)}). "
                f"Budou použity výchozí hodnoty."
            )

        try:
            with self._config_path.open('w') as f:
                json.dump(self.defaults, f, indent=2)
            self.cli_log.info(
                "Byl vytvořen nový konfigurační soubor s výchozími hodnotami.")
        except Exception as e:
            self.cli_log.warning(
                f"Nepodařilo se vytvořit konfigurační soubor ({str(e)}). "
                f"Program bude fungovat s výchozími hodnotami, ale nebude je možné trvale uložit."
            )

        return self.defaults