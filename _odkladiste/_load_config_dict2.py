class LoadConfigDictMixin:

    def _load_config_dict(self) -> Dict[str, Union[int, str, bool]]:
        """
        Načte konfiguraci ze souboru nebo vytvoří výchozí.

        Returns:
            Dict: Načtená nebo výchozí konfigurace
        """
        # Načti nebo vytvoř slovník
        config_dict = self._read_and_validate_config_file()

        # Pokud je potřeba vytvořit nový soubor, pokus se jej uložit
        if config_dict is None or self._requires_new_file(config_dict):
            config_dict = self.defaults
            self._save_new_config_file(config_dict)

        # Info o nemožnosti uložit změny
        if not self._can_save_config_file():
            self.cli_log.info("Konfigurace poběží bez možnosti uložit změny.")

        return config_dict

    def _read_and_validate_config_file(self) -> Optional[
        Dict[str, Union[int, str, bool]]]:
        """Načte a validuje konfiguraci ze souboru."""
        if not self._config_path.exists():
            return None

        try:
            config_dict = read_config_file(self._config_path)
            self._validate_config_dict(config_dict)
            return config_dict
        except Exception as e:
            self.cli_log.warning(f"Chyba při načítání: {e}", extra=e.extra)
            return None

    def _validate_config_dict(self, config_dict: Dict[
        str, Union[int, str, bool]]) -> None:
        """Validuje formát a obsah konfiguračního slovníku."""
        validate_dict_format(config_dict)
        for key, value in config_dict.items():
            validate_key_and_value(key, value)
        if not config_dict_has_all_default_keys(config_dict, self.defaults):
            config_dict = merge_with_defaults(config_dict, self.defaults)

    def _save_new_config_file(self, config_dict: Dict[
        str, Union[int, str, bool]]) -> None:
        """Uloží nový konfigurační soubor."""
        try:
            delete_config_file(self._config_path)
            save_config_file(self._config_path, config_dict)
        except Exception as e:
            self.cli_log.warning(f"Chyba při ukládání: {e}", extra=e.extra)

    def _requires_new_file(self, config_dict: Dict[
        str, Union[int, str, bool]]) -> bool:
        """Určuje, zda je potřeba vytvořit nový soubor."""
        return config_dict != merge_with_defaults(config_dict, self.defaults)

    def _can_save_config_file(self) -> bool:
        """Kontroluje, zda je možné uložit konfiguraci."""
        return self._config_path.exists()
