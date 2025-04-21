from dataclasses import dataclass
from typing import Callable, Any,Optional


@dataclass
class TypeValidator:
    description: Optional[str]
    validate_type: Callable[[Any], bool]
    validate_items: Callable[..., bool]


