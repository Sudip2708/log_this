from abc import ABC

class BaseCLIException(Exception, ABC):
    """Abstraktní základní třída pro vlastní CLI výjimky."""

    def __init__(
            self,
            message: str,
            detail: str | tuple[str, ...],
            hint: str | tuple[str, ...]
    ):
        """Uloží základní informace o chybě."""
        super().__init__(message)
        self._detail = detail
        self._hint = hint

    @property
    def detail(self) -> str | tuple[str, ...]:
        """Podrobnosti o výjimce vhodné pro CLI logging."""
        return self._detail

    @property
    def hint(self) -> str | tuple[str, ...]:
        """Tip nebo nápověda, jak chybu vyřešit."""
        return self._hint
