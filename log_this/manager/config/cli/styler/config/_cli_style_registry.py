from ._cli_style import CliStyle

# Definice konfigurací stylů
CLI_STYLE_REGISTRY = {
    '': CliStyle(
        symbol="",
        info=("",),
        detail=("",),
        hint=("",)
    ),
    'title': CliStyle(
        symbol="",
        info=("fg:blue", "bold", "underline"),
        detail=("fg:blue",),
        hint=("fg:gray",)
    ),
    'info': CliStyle(
        symbol="ℹ",
        info=("fg:blue",),
        detail=("fg:lightblue",),
        hint=("fg:gray",)
    ),
    'warning': CliStyle(
        symbol="⚠",
        info=("fg:yellow", "bold"),
        detail=("fg:yellow",),
        hint=("fg:gray",)
    ),
    'error': CliStyle(
        symbol="✘",
        info=("fg:red", "bold"),
        detail=("fg:red",),
        hint=("fg:gray",)
    ),
    'critical': CliStyle(
        symbol="✘",
        info=("fg:red", "bold", "italic"),
        detail=("fg:lightred",),
        hint=("fg:gray",)
    ),
    'success': CliStyle(
        symbol="✔",
        info=("fg:green",),
        detail=("fg:lightgreen",),
        hint=("fg:gray",)
    ),
    'help': CliStyle(
        symbol="?",
        info=("fg:cyan",),
        detail=("fg:lightcyan",),
        hint=("fg:gray",)
    )
}
