# from .static_methods import (
#     ReadConfigFileMixin,
#     SaveConfigToFileMixin
# )
from .class_methods import (
    GetConfigFilePathMixin,
    ValidateKeyAndValueMixin,
    ValidateConfigDictMixin
)
from .instance_methods2 import (
    LoadDefaultConfigMixin,
    ResetConfigMixin,
    UpdateConfigMixin,
    UpdateConfigsMixin,
    ImportConfigFromFileMixin,
    ExportConfigToFileMixin
)
from .dunder_methods import (
    StrMixin,
    GetItemMixin,
)


class ConfigMixin(

    # Inicializační metody:
    GetConfigFilePathMixin,
    # ReadConfigFileMixin,
    ValidateKeyAndValueMixin,
    ValidateConfigDictMixin,
    # SaveConfigToFileMixin,
    LoadDefaultConfigMixin,

    # Metody pro nastavení konfigurace:
    UpdateConfigMixin,
    UpdateConfigsMixin,
    ResetConfigMixin,

    # Metody pro import a export dat:
    ImportConfigFromFileMixin,
    ExportConfigToFileMixin,

    # Magické metody:
    StrMixin,
    GetItemMixin,

):
    """
    Mixin pro třídu LogThisConfig předávající ji veškeré metody.

    (Metody jsou seřazeny dle závislostí ve voláních.)

    # Inicializační metody
    - GetConfigFilePathMixin: Určí cestu ke konfiguračnímu souboru.
    - ReedConfigFileMixin: Uloží konfiguraci do souboru ve formátu JSON.
    - ValidateValueMixin: Validuje konfigurační hodnotu pro daný klíč.
    - KeyAndValueCheckMixin: Ověří platnost klíče a hodnoty konfigurace.
    - ValidateConfigDictMixin: Metoda pro ověření klíčů a hodnot konfiguračního slovníku.
    - SaveConfigToFileMixin: Aktualizuje hodnotu konfigurace a uloží ji.
    - LoadDefaultConfigMixin: Načte konfiguraci ze souboru nebo vytvoří výchozí.

    # Metody pro nastavení konfigurace:
    - UpdateConfigMixin: Aktualizuje hodnotu konfigurace a uloží ji.
    - UpdateConfigsMixin: Aktualizuje více konfiguračních hodnot najednou.
    - ResetConfigMixin: Resetuje konfiguraci na výchozí hodnoty.

    # Metody pro import a export dat:
    - ImportConfigFromFileMixin: Importuje konfiguraci z externího souboru.
    - ExportConfigToFileMixin: Exportuje aktuální konfiguraci do samostatného souboru.

    # Magické metody
    - StrMixin: Vrací čitelnou reprezentaci konfigurace.
    - GetItemMixin: Vrací hodnotu pro daný klíč.
    """
    pass