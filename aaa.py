import timeit

import functools
@functools.lru_cache(maxsize=1024)
def make_key_from_annotation_split(annotation) -> str:
    """Vrací zjednodušený klíč typu z anotace pomocí split metod."""
    s = str(annotation)
    s = s.split('[', 1)[0]
    s = s.rsplit('.', 1)[-1]
    return s.strip().lower()



def make_key_from_annotation_index(annotation) -> str:
    """Vrací zjednodušený klíč typu z anotace pomocí manipulace s indexy."""
    s = str(annotation)

    bracket_index = s.find('[')
    if bracket_index != -1:
        s = s[:bracket_index]

    dot_index = s.rfind('.')
    if dot_index != -1:
        s = s[dot_index + 1:]

    return s.strip().lower()


# Testovací anotace pokrývající různé případy
test_annotations = [
    "Mapping[str, int]",
    "typing.Mapping[str, int]",
    "collections.abc.Mapping[str, int]",
    "Mapping",
    "typing.Mapping",
    "collections.abc.Mapping",
    "List[Union[Dict[str, Any], Set[Tuple[int, float]]]]"
]


# Měření času pro metodu se split
def test_split():
    for ann in test_annotations:
        make_key_from_annotation_split(ann)


# Měření času pro metodu s indexy
def test_index():
    for ann in test_annotations:
        make_key_from_annotation_index(ann)


# Měření času
split_time = timeit.timeit(test_split, number=1000000)
index_time = timeit.timeit(test_index, number=1000000)

print(f"Implementace se split: {split_time:.6f} s")
print(f"Implementace s indexy: {index_time:.6f} s")
print(f"Poměr: {split_time / index_time:.2f}x")