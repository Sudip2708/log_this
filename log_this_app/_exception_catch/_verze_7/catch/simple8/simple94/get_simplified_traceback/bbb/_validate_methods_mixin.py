from ._input_error import GetSimplifiedTracebackInputError


class ValidateMethodsMixin:

    @staticmethod
    def _validate_skip_lines(skip_lines: int) -> int:
        """
        Ověří, že skip_lines je platné celé kladné číslo.

        Args:
            skip_lines: Hodnota k ověření

        Returns:
            Ověřená hodnota skip_lines

        Raises:
            GetSimplifiedTracebackInputError: Pokud skip_lines není celé kladné číslo
        """
        if not isinstance(skip_lines, int) or skip_lines < 0:
            raise GetSimplifiedTracebackInputError(
                parameter="skip_lines",
                input_value=skip_lines,
                allowed_value="Celé kladné číslo",
                description="Určuje počet záznamů od konce, "
                            "které se mají ve výpisu vynechat."
            )
        return skip_lines

    @staticmethod
    def _validate_users_code_only(users_code_only: bool) -> bool:
        """
        Ověří, že users_code_only je platná booleovská hodnota.

        Args:
            users_code_only: Hodnota k ověření

        Returns:
            Ověřená hodnota users_code_only

        Raises:
            GetSimplifiedTracebackInputError: Pokud users_code_only není boolean
        """
        if not isinstance(users_code_only, bool):
            raise GetSimplifiedTracebackInputError(
                parameter="users_code_only",
                input_value=users_code_only,
                allowed_value="True / False",
                description="Určuje zda se mají vypsat pouze uživatelovo záznamy, "
                            "nebo všechny."
            )
        return users_code_only

    @staticmethod
    def _validate_lines_limit(lines_limit: Union[bool, int]) -> Union[
        bool, int]:
        """
        Ověří, že lines_limit je platná hodnota.

        Args:
            lines_limit: Hodnota k ověření

        Returns:
            Ověřená hodnota lines_limit

        Raises:
            GetSimplifiedTracebackInputError: Pokud lines_limit není boolean nebo kladné číslo
        """
        if isinstance(lines_limit, bool):
            return lines_limit
        elif isinstance(lines_limit, int) and lines_limit >= 0:
            return lines_limit
        else:
            raise GetSimplifiedTracebackInputError(
                parameter="lines_limit",
                input_value=lines_limit,
                allowed_value="False pro všechny záznamy, "
                              "jinak celé kladné číslo pro definici počtu.",
                description="Určuje počet záznamů, které se mají vypsat."
            )