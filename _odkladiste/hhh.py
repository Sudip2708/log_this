import re
from typing import Any, Set, Union, Tuple, Optional
from collections.abc import Iterable
from _odkladiste._ansi_codes import TEXT_STYLES, TEXT_COLORS, BACKGROUND_COLORS

AnsiCode = Union[int, str]
AnsiCodes = Union[AnsiCode, Tuple[AnsiCode, ...], Set[AnsiCode], list[AnsiCode]]


def list_of_allowed_codes() -> Set[str]:
    """
    Returns a set of all valid ANSI codes from text styles, colors and background colors.

    Returns:
        Set[str]: A set containing all valid ANSI codes as strings.
    """
    dictionary = {**TEXT_STYLES, **TEXT_COLORS, **BACKGROUND_COLORS}
    return set(dictionary.values())


def check_codes(codes: Iterable[AnsiCode]) -> None:
    """
    Validates if all provided ANSI codes are allowed.

    Args:
        codes: An iterable of ANSI codes to validate.

    Raises:
        ValueError: If any code is not in the list of allowed codes.
    """
    allowed_codes = list_of_allowed_codes()
    for code in tuple(codes):
        if str(code) not in allowed_codes:
            raise ValueError(
                f"Invalid code: {code}, allowed values: {allowed_codes}"
            )


def wrap_with_codes(text: str, codes: Optional[AnsiCodes] = None) -> str:
    """
    Wraps text with ANSI escape sequences using the specified formatting codes.

    Args:
        text: The text to be wrapped with ANSI codes.
        codes: Single code or multiple codes to apply. Can be int, str, tuple, list, or set.
            If None or empty, returns the original text.

    Returns:
        str: Text wrapped with ANSI escape sequences.

    Raises:
        TypeError: If codes are not of the correct type or not convertible to str.
        ValueError: If any of the codes is not valid.
    """
    if codes is None or not codes:
        return text

    if isinstance(codes, (int, str)):
        check_codes((codes,))
        return f"\033[{codes}m{text}\033[0m"

    if isinstance(codes, (list, set)):
        codes = tuple(set(codes))

    if len(codes) == 1:
        check_codes(codes)
        code = codes[0]
        if not isinstance(code, (int, str)):
            raise TypeError("Code must be int or str")
        return f"\033[{code}m{text}\033[0m"

    try:
        codes_str = ";".join(str(code) for code in codes)
    except TypeError:
        raise TypeError("All codes must be convertible to str")

    check_codes(codes)
    return f"\033[{codes_str}m{text}\033[0m"


def process_text(text: str, new_codes: AnsiCodes) -> str:
    """
    Processes text containing ANSI sequences and adds new formatting codes to unformatted parts.

    This function preserves existing ANSI formatting while adding new formatting codes
    to unformatted text segments. It handles nested and multiple ANSI codes properly.

    Args:
        text: Input text that may contain ANSI escape sequences.
        new_codes: New formatting codes to apply to unformatted text segments.
            Can be a single code or multiple codes.

    Returns:
        str: Processed text with both existing and new ANSI formatting applied.

    """
    pattern = re.compile(r"\033\[[0-9;]*m|[^\033]+")
    current_codes: Set[str] = set()
    result: list[str] = []

    for match in pattern.finditer(text):
        part = match.group(0)

        if part.startswith("\033"):
            codes = part[2:-1].split(";")

            if "0" in codes:
                current_codes.clear()
            else:
                current_codes.update(codes)
        else:
            formatted_part = (
                wrap_with_codes(part, current_codes)
                if current_codes
                else wrap_with_codes(part, new_codes)
            )
            result.append(formatted_part)

    return "".join(result)


# Testovací vstupy
vstup1 = "Toto je text."
vstup2 = "Toto je \033[1;31mčervený text\033[0m a další část."
vstup3 = "\033[34mModrý\033[0m text a \033[32mzelený\033[0m."

# Výsledky
print(process_text(vstup1, (31, 1)))  # Očekáváme celý text obalený červeně a tučně
print(process_text(vstup2, (34,)))    # Neformátované části obaleny modře
print(process_text(vstup3, (35, 4)))  # Neformátované části obaleny fialově a podtrženě

# Výsledky
print(repr(process_text(vstup1, (31, 1))))  # Očekáváme celý text obalený červeně a tučně
print(repr(process_text(vstup2, (34,))))    # Neformátované části obaleny modře
print(repr(process_text(vstup3, (35, 4))))  # Neformátované části obaleny fialově a podtrženě