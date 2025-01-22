from typing import Dict, Union, Optional
from pathlib import Path


class LoadConfigDictMixin:

    def _load_config_dict(self) -> Dict[str, Union[int, str, bool]]:
        """
        Načte konfiguraci ze souboru nebo vytvoří výchozí.

        Returns:
            Dict: Načtená nebo výchozí konfigurace
        """
        config_dict = self._read_existing_config()

        if not config_dict:
            config_dict = self._create_new_config()

        return config_dict

    def _read_existing_config(self) -> Optional[
        Dict[str, Union[int, str, bool]]]:
        """
        Pokusí se načíst existující konfiguraci.

        Returns:
            Optional[Dict]: Načtená konfigurace nebo None v případě chyby
        """
        if not self._config_path.exists():
            return None

        try:
            config_dict = self._load_and_validate_config()
            if self._needs_update(config_dict):
                config_dict = self._update_config(config_dict)
            return config_dict

        except (ReadConfigFileError, ValidateDictFormatError,
                ValidateKeyAndValueError, ConfigDictHasAllDefaultKeysError,
                MergeWithDefaultsError) as e:
            self._handle_read_error(e)
            return None

    def _load_and_validate_config(self) -> Dict[str, Union[int, str, bool]]:
        """
        Načte a zvaliduje konfigurační soubor.

        Returns:
            Dict: Zvalidovaná konfigurace

        Raises:
            Various validation errors
        """
        config_dict = read_config_file(self._config_path)
        validate_dict_format(config_dict)

        for key, value in config_dict.items():
            validate_key_and_value(key, value)

        return config_dict


    # def _has_all_required_keys(self, config_dict: Dict[str, Any]) -> bool:
    #     """
    #     Zkontroluje, zda konfigurace obsahuje všechny požadované klíče.
    #     """
    #     try:
    #         return set(config_dict.keys()) == set(self.defaults.keys())
    #     except (AttributeError, TypeError) as e:
    #         self._handle_validation_error("Invalid configuration structure", e)
    #         return False
    #
    # def _needs_update(self, config_dict: Dict[str, Any]) -> bool:
    #     return not self._has_all_required_keys(config_dict)

    def _needs_update(self,
                      config_dict: Dict[str, Union[int, str, bool]]) -> bool:
        """
        Zkontroluje, zda konfigurace potřebuje aktualizaci.

        Args:
            config_dict: Současná konfigurace

        Returns:
            bool: True pokud konfigurace potřebuje aktualizaci
        """
        return not config_dict_has_all_default_keys(config_dict, self.defaults)

    def _update_config(self, config_dict: Dict[str, Union[int, str, bool]])
        -> Dict[str, Union[int, str, bool]]:
        """
        Aktualizuje konfiguraci pomocí výchozích hodnot.

        Args:
            config_dict: Současná konfigurace

        Returns:
            Dict: Aktualizovaná konfigurace
        """
        updated_dict = merge_with_defaults(config_dict, self.defaults)
        self._save_config(updated_dict)
        return updated_dict

    def _create_new_config(self) -> Dict[str, Union[int, str, bool]]:
        """
        Vytvoří novou konfiguraci z výchozích hodnot.

        Returns:
            Dict: Nová konfigurace
        """
        self._cleanup_existing_file()
        config_dict = self.defaults.copy()
        self._save_config(config_dict)
        return config_dict

    def _cleanup_existing_file(self) -> None:
        """Pokusí se smazat existující konfigurační soubor."""
        try:
            if self._config_path.exists():
                delete_config_file(self._config_path)
        except DeleteConfigFileError as e:
            self._handle_delete_error(e)

    def _save_config(self,
                     config_dict: Dict[str, Union[int, str, bool]]) -> None:
        """
        Uloží konfiguraci do souboru.

        Args:
            config_dict: Konfigurace k uložení
        """
        try:
            save_config_file(self._config_path, config_dict)
        except SaveConfigError as e:
            self._handle_save_error(e)

    def _handle_read_error(self, error: Exception) -> None:
        """Zpracuje chybu při čtení konfigurace."""
        self.cli_log.warning(f"{error}", extra=error.extra)

    def _handle_delete_error(self, error: DeleteConfigFileError) -> None:
        """Zpracuje chybu při mazání souboru."""
        self.cli_log.warning(f"{error}", extra=error.extra)

    def _handle_save_error(self, error: SaveConfigError) -> None:
        """Zpracuje chybu při ukládání souboru."""
        self.cli_log.warning(f"{error}", extra=error.extra)
        self.cli_log.info(
            "Konfigurace poběží bez možnosti uložit změny.",
            extra={"hint": "Zkontrolujte oprávnění k souboru."}
        )