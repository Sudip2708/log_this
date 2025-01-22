import curses

def select_key_with_arrows(keys_data):
    """
    Umožňuje uživateli vybrat klíč pomocí šipek nahoru a dolů a potvrzení pomocí Enteru.

    Args:
        keys_data (dict): Slovník obsahující klíče a jejich popisné informace.

    Returns:
        str: Vybraný klíč odpovídající zvolenému popisnému textu.
    """
    def draw_menu(stdscr, current_idx):
        stdscr.clear()
        stdscr.addstr("\nPoužijte šipky nahoru/dolů pro výběr, Enter pro potvrzení:\n\n")

        for idx, (key, key_data) in enumerate(keys_data.items()):
            if idx == current_idx:
                stdscr.addstr(f" > {key_data['info']}\n", curses.A_REVERSE)
            else:
                stdscr.addstr(f"   {key_data['info']}\n")

        stdscr.refresh()

    def menu(stdscr):
        curses.curs_set(0)  # Skryje kurzor
        current_idx = 0
        keys = list(keys_data.keys())

        while True:
            draw_menu(stdscr, current_idx)
            key = stdscr.getch()

            if key == curses.KEY_UP and current_idx > 0:
                current_idx -= 1
            elif key == curses.KEY_DOWN and current_idx < len(keys) - 1:
                current_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter key
                return keys[current_idx]

    return curses.wrapper(menu)

# Příklad použití
if __name__ == "__main__":
    examplekeys_data = {
        "indent": {"info": "Nastavení pro odsazení (indent)."},
        "blank_lines": {"info": "Zobrazení prázdných řádků mezi logy."},
        "max_depth": {"info": "Maximální hloubka rekurze."},
    }

    selected_key = select_key_with_arrows(examplekeys_data)
    print(f"Vybraný klíč: {selected_key}")
