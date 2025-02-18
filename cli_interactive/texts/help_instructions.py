from cli_styler import INFO, END_LINE, LIST, EMPTY_LINE

HELP_INSTRUCTION = [
    ('class:hint.title', f'{INFO}NÁPOVĚDA:{END_LINE}'),
    ('class:hint.offer', f'{LIST}Použijte šipky ↑↓ pro výběr položky{END_LINE}'),
    ('class:hint.offer', f'{LIST}Stiskněte Enter pro potvrzení výběru{END_LINE}'),
    ('class:hint.offer', f'{LIST}Ctrl+C pro ukončení{END_LINE}'),
    ('', f'{EMPTY_LINE}')
]
def set_hint_title(title):
    return "class:hint.title", f"{INFO}{title}{END_LINE}"

def set_hint_offer(text):
    return "class:hint.offer", f"{LIST}{text}{END_LINE}"

def set_empty_line():
    return "class:", f"{EMPTY_LINE}"

def get_help_instruction():
    return [
        set_hint_title("NÁPOVĚDA:"),
        set_hint_offer("Použijte šipky ↑↓ pro výběr položky"),
        set_hint_offer("Stiskněte Enter pro potvrzení výběru"),
        set_hint_offer("Ctrl+C pro ukončení"),
        set_empty_line()
    ]

