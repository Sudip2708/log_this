from typing import Union, Type
import typing


def get_typing_code(annotation: Union[typing, Type]):
    """Funkce na převod anotace knihovny typing na tuple hodnot"""

    # Převod na řetězec a malé písmena
    string = str(annotation).lower()

    # Odstranění případných výskytů typing
    string = string.replace("typing.", "")

    # Obalení hramatých závorek čárkami
    string = string.replace("[", ",[,")
    string = string.replace("]", ",],")

    # Vymazání prázdných míst
    string = string.replace(" ", "")

    # Odstranění zdvojených čárek
    while ",," in string:
        string = string.replace(",,", ",")

    # Odstranění případné koncové čárky
    string = string[:-1] if string[-1] == "," else string

    # Navrácení tuple s hodnotami
    return tuple(string.split(","))



# Příklad použití
if __name__ == "__main__":
    # Příklady parsování typových anotací
    examples = [
        typing.List[str],
        typing.List[typing.Union[int, str]],
        typing.Dict[str, int],
        typing.Tuple[int, str, bool],
        typing.Tuple[int, ...],
        typing.Union[int, str, None],
        typing.Optional[int],
        typing.Literal[1, 2, 3],
        typing.Callable[[int, str], bool],
        typing.Sequence[int],
    ]

    # for example in examples:
    #     print(f"{example} => {parse_typing_annotation(example)}")

    # Příklady kontrol typů
    test_cases = [
        (["hello", "world"], typing.List[str]),
        (["hello", 123], typing.List[typing.Union[str, int]]),
        ({"name": "John", "age": 30}, typing.Dict[str, int]),
        ((1, "hello", True), typing.Tuple[int, str, bool]),
        ((1, 2, 3), typing.Tuple[int, ...]),
        (42, typing.Union[int, str, None]),
        (None, typing.Optional[int]),
        (2, typing.Literal[1, 2, 3]),
        (lambda x, y: x == y, typing.Callable[[int, str], bool]),
        ([1, 2, 3], typing.Sequence[int]),
    ]

    for value, type_annotation in test_cases:

        # result = check_type(value, type_annotation)
        # print(f"Hodnota {value} odpovídá typu {type_annotation}? {result}")

        result = parse_typing_annotation(type_annotation)
        print(f"Výstup pro: {type_annotation} >>> {result}")