from abc import ABC, abstractmethod
from .mixins import (
    ShowHelpMixin,
    ShowSuccessMenuMixin,
    ValidateAndSaveMixin,
    ConvertValueMixin,
    InputConfigValueMixin,
    SelectConfigKeyMixin,
    ConfigSettingsMixin,
    MainMenuMixin,
)

class AllMixins(
    ABC,
    ShowHelpMixin,
    ShowSuccessMenuMixin,
    ValidateAndSaveMixin,
    ConvertValueMixin,
    InputConfigValueMixin,
    SelectConfigKeyMixin,
    ConfigSettingsMixin,
    MainMenuMixin,
):

    pass