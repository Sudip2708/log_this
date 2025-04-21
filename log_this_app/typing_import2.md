# Rozšířený přehled typů z knihovny typing

| Název typu | Import | Konkrétní typy a jejich použití |
|------------|--------|--------------------------------|
| ABCMeta | from abc import ABCMeta | |
| Annotated | from typing import Annotated | Annotated[T, ...] |
| Any | from typing import Any | Any |
| AnyStr | from typing import AnyStr | AnyStr (TypeVar omezený na str/bytes) |
| BinaryIO | from typing import BinaryIO | |
| Callable | from typing import Callable | Callable[..., R] |
| ClassVar | from typing import ClassVar | ClassVar[T] |
| Concatenate | from typing import Concatenate | Concatenate[...] |
| ContextManager | from typing import ContextManager | ContextManager[T] |
| Coroutine | from typing import Coroutine | Coroutine[Y, S, R] |
| Counter | from collections import Counter | Counter[T] |
| DefaultDict | from collections import defaultdict | DefaultDict[K, V] |
| Deque | from collections import deque | Deque[T] |
| Dict | from typing import Dict | Dict[K, V] |
| Final | from typing import Final | Final |
| ForwardRef | from typing import ForwardRef * | |
| FrozenSet | from typing import FrozenSet | FrozenSet[T] |
| Generator | from typing import Generator | Generator[Y, S, R] |
| Generic | from typing import Generic | Generic |
| GenericAlias | from types import GenericAlias | |
| IO | from typing import IO | |
| Iterable | from typing import Iterable | Iterable[T] |
| Iterator | from typing import Iterator | Iterator[T] |
| AsyncIterable | from typing import AsyncIterable | AsyncIterable[T] |
| AsyncIterator | from typing import AsyncIterator | AsyncIterator[T] |
| AsyncContextManager | from typing import AsyncContextManager | AsyncContextManager[T] |
| List | from typing import List | List[T] |
| Literal | from typing import Literal | Literal[...] |
| LiteralString | from typing import LiteralString | |
| Mapping | from typing import Mapping | Mapping[K, V] |
| MutableMapping | from typing import MutableMapping | MutableMapping[K, V] |
| MethodDescriptorType | * (interní typ Pythonu) | |
| MethodWrapperType | * (interní typ Pythonu) | |
| NamedTupleMeta | * (interní implementace) | |
| NamedTuple | from typing import NamedTuple | NamedTuple |
| Never | from typing import Never | |
| NewType | from typing import NewType | NewType |
| NoReturn | from typing import NoReturn | NoReturn |
| NotRequired | from typing import NotRequired | |
| Optional | from typing import Optional | Optional[T] |
| OrderedDict | from collections import OrderedDict | OrderedDict[K, V] |
| ParamSpec | from typing import ParamSpec | |
| ParamSpecArgs | from typing import ParamSpecArgs * | |
| ParamSpecKwargs | from typing import ParamSpecKwargs * | |
| Protocol | from typing import Protocol | Protocol |
| Required | from typing import Required | |
| Self | from typing import Self | Self |
| Sequence | from typing import Sequence | Sequence[T] |
| Set | from typing import Set | Set[T] |
| SupportsAbs | from typing import SupportsAbs | |
| SupportsBytes | from typing import SupportsBytes | |
| SupportsComplex | from typing import SupportsComplex | |
| SupportsFloat | from typing import SupportsFloat | |
| SupportsIndex | from typing import SupportsIndex | |
| SupportsInt | from typing import SupportsInt | |
| SupportsRound | from typing import SupportsRound | |
| Text | built-in typ `str` | |
| TextIO | from typing import TextIO | |
| Tuple | from typing import Tuple | Tuple[T1, T2, ...], Tuple[T, ...] |
| Type | from typing import Type | Type[T] |
| TypeAlias | from typing import TypeAlias | |
| TypeGuard | from typing import TypeGuard | |
| TypeVar | from typing import TypeVar | TypeVar |
| TypeVarTuple | from typing import TypeVarTuple | |
| TypedDict | from typing import TypedDict | TypedDict |
| Union | from typing import Union | Union[T1, T2, ...] |
| Unpack | from typing import Unpack | |
| WrapperDescriptorType | * (interní typ Pythonu) | |
| ChainMap | from collections import ChainMap | ChainMap[K, V] |
| _AnnotatedAlias | * (interní implementace) | |
| _AnyMeta | * (interní implementace) | |
| _BaseGenericAlias | * (interní implementace) | |
| _BoundVarianceMixin | * (interní implementace) | |
| _CallableGenericAlias | * (interní implementace) | |
| _CallableType | * (interní implementace) | |
| _ConcatenateGenericAlias | * (interní implementace) | |
| _DeprecatedType | * (interní implementace) | |
| _Final | * (interní implementace) | |
| _GenericAlias | * (interní implementace) | |
| _Immutable | * (interní implementace) | |
| _LiteralGenericAlias | * (interní implementace) | |
| _LiteralSpecialForm | * (interní implementace) | |
| _NamedTuple | from typing import NamedTuple | |
| _NotIterable | * (interní implementace) | |
| _PickleUsingNameMixin | * (interní implementace) | |
| _ProtocolMeta | * (interní implementace) | |
| _SpecialForm | * (interní implementace) | |
| _SpecialGenericAlias | * (interní implementace) | |
| _TupleType | * (interní implementace) | |
| _TypedDict | from typing import TypedDict | |
| _TypedDictMeta | * (interní implementace) | |
| _TypingEllipsis | * (interní implementace) | |
| _UnionGenericAlias | * (interní implementace) | |
| _UnpackGenericAlias | * (interní implementace) | |
| _alias | * (interní implementace) | |
| defaultdict | from collections import defaultdict | |
| io | from typing import io * (zastaralé) | |
| re | from typing import re * (zastaralé) | |