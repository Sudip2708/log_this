from prompt_toolkit import print_formatted_text, HTML

# Definice barev
COLORS = {
    "RED": ("#ff8787", "#cc5c5c"),
    "RED_ORANGE": ("#ff9b73", "#d67b56"),
    "ORANGE": ("#ffb56b", "#d98a4d"),
    "ORANGE_YELLOW": ("#ffcf6b", "#d4a74d"),
    "YELLOW": ("#ffeb6b", "#c2b84d"),
    "YELLOW_GREEN": ("#c8e87b", "#97b95c"),
    "GREEN": ("#66cc66", "#4d994d"),
    "GREEN_BLUE": ("#5dc9c9", "#449999"),
    "BLUE": ("#268bd2", "#1f6ea5"),
    "BLUE_VIOLET": ("#a29bfe", "#826ab1"),
    "VIOLET": ("#bf7fff", "#6c71c4"),
}

def print_color_test():
    """Vytiskne seznam barev v terminálu ve formátu:
    - Světlý odstín jako velký bold text
    - Tmavý odstín jako malý normální text
    """
    for name, (light, dark) in COLORS.items():
        print_formatted_text(HTML(f'<b><style fg="{light}"> {name}-LIGHT </style></b>'))
        print_formatted_text(HTML(f'<style fg="{dark}"> {name}-DARK </style>'))
        print()  # Prázdný řádek pro oddělení

if __name__ == "__main__":
    print_color_test()
