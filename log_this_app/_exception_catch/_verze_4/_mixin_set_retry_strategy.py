from typing import Any, Tuple, Type

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .exception_handler import ExceptionHandler

from abc_helper import ABC, abc_property


class RetryableException(Exception):
    """Výjimka indikující možnost opakování."""
    pass


class SetRetryStrategyMixin(ABC):


    def set_retry_strategy(
            self,
            exception_type: Type[Exception],
            max_attempts: int = 3,
            delay: float = 1.0,
            backoff_factor: float = 2.0,
            retriable_exceptions: Tuple[Type[Exception], ...] = (RetryableException,)
    ) -> 'ExceptionHandler':
        """
        Nastavení strategie opakování pro specifické výjimky.

        :param exception_type: Typ výjimky pro strategii opakování
        :param max_attempts: Maximální počet opakování
        :param delay: Počáteční prodleva mezi pokusy
        :param backoff_factor: Faktor pro exponenciální nárůst prodlevy
        :param retriable_exceptions: Typy výjimek, které umožňují opakování
        :return: Instance ExceptionHandleru
        """

        self._retry_strategies[exception_type] = {
            'max_attempts': max_attempts,
            'delay': delay,
            'backoff_factor': backoff_factor,
            'retriable_exceptions': retriable_exceptions
        }

        return self