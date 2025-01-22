import pytest
from log_this.manager.config.init_mixins import ConfigMixin
from log_this.manager.config.init_mixins.static_methods import (
    ReadConfigFileMixin,
    SaveConfigToFileMixin
)
from log_this.manager.config.init_mixins.class_methods import (
    GetConfigFilePathMixin,
    KeyAndValueCheckMixin,
    ValidateValueMixin,
    ValidateConfigDictMixin
)
from log_this.manager.config.init_mixins.instance_methods2 import (
    LoadDefaultConfigMixin,
    ResetConfigMixin,
    UpdateConfigMixin,
    UpdateConfigsMixin,
    ImportConfigFromFileMixin,
    ExportConfigToFileMixin
)
from log_this.manager.config.init_mixins.dunder_methods import (
    StrMixin,
    GetItemMixin,
)


# Test správného pořadí dědičnosti
def test_inheritance_order():
    # Ověříme, zda ConfigMixin dědí od správného pořadí mixinů
    assert issubclass(ConfigMixin, GetConfigFilePathMixin)
    assert issubclass(ConfigMixin, ReadConfigFileMixin)
    assert issubclass(ConfigMixin, ValidateValueMixin)
    assert issubclass(ConfigMixin, KeyAndValueCheckMixin)
    assert issubclass(ConfigMixin, ValidateConfigDictMixin)
    assert issubclass(ConfigMixin, SaveConfigToFileMixin)
    assert issubclass(ConfigMixin, LoadDefaultConfigMixin)
    assert issubclass(ConfigMixin, UpdateConfigMixin)
    assert issubclass(ConfigMixin, UpdateConfigsMixin)
    assert issubclass(ConfigMixin, ResetConfigMixin)
    assert issubclass(ConfigMixin, ImportConfigFromFileMixin)
    assert issubclass(ConfigMixin, ExportConfigToFileMixin)
    assert issubclass(ConfigMixin, StrMixin)
    assert issubclass(ConfigMixin, GetItemMixin)


# Test, že nedochází ke konfliktům metod
def test_no_method_conflicts():
    # Získáme seznam všech metod ve třídě ConfigMixin
    config_mixin_methods = dir(ConfigMixin)

    # Seznam metod z jednotlivých mixinů, které by neměly být v konfliktu
    expected_methods = [
        '_get_config_file_path',
        '_read_config_file',
        '_validate_value',
        '_key_and_value_check',
        '_validate_config_dict',
        '_save_config_to_file',
        '_load_default_config',
        'update_config',
        'update_configs',
        'reset_config',
        'import_config_from_file',
        'export_config_to_file',
        '__str__',
        '__getitem__'
    ]

    # Ověříme, že všechny očekávané metody existují v ConfigMixin
    for method in expected_methods:
        assert method in config_mixin_methods, f"Method {method} is missing in ConfigMixin"

    # Ověříme, že nejsou žádné metody s duplikátním názvem
    method_counts = {method: config_mixin_methods.count(method) for method in
                     config_mixin_methods}
    for method, count in method_counts.items():
        assert count == 1, f"Method {method} appears more than once"

