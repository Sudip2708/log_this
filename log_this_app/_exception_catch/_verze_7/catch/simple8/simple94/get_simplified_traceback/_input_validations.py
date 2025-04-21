from ._input_error import GetSimplifiedTracebackInputError

def _get_skip_lines(skip_lines):
    if not isinstance(skip_lines, int) and skip_lines < 0:
        raise GetSimplifiedTracebackInputError(
            parameter="skip_lines",
            input_value=skip_lines,
            allowed_value="Celé kladné číslo",
            description="Určuje počet záznamů od konce, "
                        "které se mají ve výpisu vynechat."
        )
    return skip_lines


def _get_users_code_only(users_code_only):
    if not isinstance(users_code_only, bool):
        raise GetSimplifiedTracebackInputError(
            parameter="users_code_only",
            input_value=users_code_only,
            allowed_value="True / False",
            description="Určuje zda se mají vypsat pouze uživatelovo záznamy, "
                        "nebo všechny."
        )
    return users_code_only


def _get_lines_limit(lines_limit):
    if not isinstance(lines_limit, bool) or (
            not isinstance(lines_limit, int) and lines_limit < 0
    ):
        raise GetSimplifiedTracebackInputError(
            parameter="lines_limit",
            input_value=lines_limit,
            allowed_value="False pro všechny záznamy, "
                          "jinak celé kladné číslo pro definici počtu.",
            description="Určuje počet záznamů, které se mají vypsat."
        )
    return lines_limit