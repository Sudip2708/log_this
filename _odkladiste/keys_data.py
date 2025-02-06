from .keys_data_mixins import (
    SkipThisKey,
    OneLineKey,
    SimpleKey,
    DetailedKey,
    ReportKey,
    TrueKey,
    FalseKey,
    NoneKey,
    EmptyKey,
    IndentKey,
    BlankLinesKey,
    DocstringLinesKey,
    MaxDepthKey,
)

KEYS_DATA = {
    'skip_this': SkipThisKey(),
    'one_line': OneLineKey(),
    'simple': SimpleKey(),
    'detailed': DetailedKey(),
    'report': ReportKey(),
    'true': TrueKey(),
    'false': FalseKey(),
    'none': NoneKey(),
    'empty': EmptyKey(),
    'indent': IndentKey(),
    'blank_lines': BlankLinesKey(),
    'docstring_lines': DocstringLinesKey(),
    'max_depth': MaxDepthKey()
}


