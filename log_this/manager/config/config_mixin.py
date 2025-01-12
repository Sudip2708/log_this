from .mixins import (
    # Class methods:
    CreateConfigFileMixin,
    DeleteConfigFileMixin,
    LoadConfigDictMixin,
    ReadConfigFileMixin,
    ValidateKeyAndValueMixin,
    ValidateConfigDictMixin,
    # Dunder methods:
    GetItemMixin,
    StrMixin,
    # Instance methods:
    ExportConfigToFileMixin,
    ImportConfigFromFileMixin,
    ResetToDefaultMixin,
    SetNewValueMixin,
    ShowConfigMixin
)

class ConfigMixin(
    # Class methods:
    CreateConfigFileMixin,
    DeleteConfigFileMixin,
    LoadConfigDictMixin,
    ReadConfigFileMixin,
    ValidateKeyAndValueMixin,
    ValidateConfigDictMixin,
    # Dunder methods:
    GetItemMixin,
    StrMixin,
    # Instance methods:
    ExportConfigToFileMixin,
    ImportConfigFromFileMixin,
    ResetToDefaultMixin,
    SetNewValueMixin,
    ShowConfigMixin

):
    """
    Mixin pro třídu LogThisConfig předávající ji veškeré metody.

    (Metody jsou seřazeny dle závislostí ve voláních.)

    # Class methods:
        - CreateConfigFileMixin: Metoda pro vytvoření konfiguračního souboru.
        - DeleteConfigFileMixin: Metoda pro smazání konfiguračního souboru.
        - LoadConfigDictMixin: Načte konfiguraci ze souboru nebo vytvoří výchozí.
        - ReadConfigFileMixin: Reads a configuration file and returns a dictionary with configurations.
        - ValidateKeyAndValueMixin: Validuje konfigurační hodnotu pro daný klíč.
        - ValidateConfigDictMixin: Metoda pro ověření klíčů a hodnot konfiguračního slovníku.

    # Dunder methods:
        - StrMixin: Vrací čitelnou reprezentaci konfigurace.
        - GetItemMixin: Vrací hodnotu pro daný klíč.

    # Instance methods:
        - ExportConfigToFileMixin: Metoda pro uložení konfigurace do externího souboru
        - ImportConfigFromFileMixin: Metoda pro nahrání konfigurace z externího souboru
        - ResetToDefaultMixin: Metoda pro resetování konfigurace na výchozí hodnoty
        - SetNewValueMixin: Metoda pro změnu jedné položky konfigurace
        - ShowConfigMixin: Metoda pro vypsání aktuálního stavu konfigurace
    """
    pass