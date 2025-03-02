from ._main_menu import MainMenu
from ._exit_menu import ExitMenu
from ._config_menu import ConfigMenu
from ._config_key_select import ConfigKeySelect
from ._config_value_select import ConfigValueSelect
from ._menus_config_menu import MenusConfigMenu
from ._menus_config_symbols_select import MenusConfigSymbolsSelect
from ._menus_config_colors_select import MenusConfigColorsSelect


def get_menus_dict(cli):

    return {
        "main_menu": MainMenu(cli),
        "exit_menu": ExitMenu(cli),
        "config_menu": ConfigMenu(cli),
        "config_key_select": ConfigKeySelect(cli),
        "config_value_select": ConfigValueSelect(cli),
        "menus_config": MenusConfigMenu(cli),
        "menus_symbols_select": MenusConfigSymbolsSelect(cli),
        "menus_colors_select": MenusConfigColorsSelect(cli),
    }