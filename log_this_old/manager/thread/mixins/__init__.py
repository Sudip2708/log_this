from ._increase_depth_and_update_type import IncreaseDepthAndUpdateTypeMixin
from ._decrease_depth import DecreaseDepthMixin

__all__ = [
    "IncreaseDepthAndUpdateTypeMixin",  # Navýší hloubku zanoření a zaznamená hodnotu mode.
    "DecreaseDepthMixin",  # Sníží hodnotu hloubky zanoření.
]