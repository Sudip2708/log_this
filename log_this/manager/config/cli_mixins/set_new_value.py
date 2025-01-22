from abc import ABC, abstractmethod
from typing import Union

from ..errors import ValidateKeyError, ValidateValueError


class SetNewValueMixin(ABC):

    @abstractmethod
    def _validate_key_and_value(self, key: str, value: Union[int, str, bool]) -> None:
        """Validuje konfigurační klíč a hodnotu."""
        pass

    @property
    @abstractmethod
    def cli_log(self) -> logging.Logger:
        """Logger pro CLI komunikaci."""
        pass

    @property
    @abstractmethod
    def config(self) -> Dict[str, Union[int, str, bool]]:
        pass

    # @abstractmethod
    # def create_config_file(self) -> bool:
    #     """Vytvoří novou konfiguraci z výchozích hodnot."""
    #     pass

    def set_new_value(
            self,
            key: str,
            value: Union[int, str, bool],
            value_check: bool = False
    ) -> None:

        # Kontrola zda ještě není provedena validace
        if not value_check:

            # Kontrola klíče a hodnoty
            try:
                self._validate_key_and_value(key, value)
            # Zachycení špatného klíče a hodnoty
            except (ValidateKeyError, ValidateValueError) as e:
                extra = getattr(e, "extra", {})
                self.cli_log.error(e, extra=extra)

            # Kontrola, zda již hodnota nebyla aktualizovaná
            if self.config[key] == value:
                print(f"\nThe configuration key '{key}' is already set to '{value}'. \n"
                      f"Žádná změna nebyla učiněna. \n")
                return

        # Uložení změny do instance třídy
        self.config[key] = value
        print("Byla změněna konfigurace pro klíč '{key}' na hodnotu: {value}")

        # Nastavení atribut deklarujícího vytvoření nového souboru
        self._create_config_file = True

        # Uložení změny do konfiguračního souboru
        self.create_config_file()
        print("Změna konfigurace byla zapsaná do konfiguračního souboru")




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