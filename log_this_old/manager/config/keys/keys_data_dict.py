from .data import (
    IndentKey,
    BlankLinesKey,
    DocstringLinesKey,
    MaxDepthKey,
    SkipThisKey,
    OneLineKey,
    SimpleKey,
    DetailedKey,
    ReportKey,
    TrueKey,
    FalseKey,
    NoneKey,
    EmptyKey
)

KEYS_DATA = {
    'indent': IndentKey(),
    'blank_lines': BlankLinesKey(),
    'docstring_lines': DocstringLinesKey(),
    'max_depth': MaxDepthKey(),
    'skip_this': SkipThisKey(),
    'one_line': OneLineKey(),
    'simple': SimpleKey(),
    'detailed': DetailedKey(),
    'report': ReportKey(),
    'true': TrueKey(),
    'false': FalseKey(),
    'none': NoneKey(),
    'empty': EmptyKey(),
}


