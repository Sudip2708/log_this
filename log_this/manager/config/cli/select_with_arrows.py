import curses


def select_with_arrows(options):
    """
    Interaktivní výběr ze seznamu pomocí šipek nahoru a dolu.
    Entrem potvrdíte volbu.
    """
    def menu(stdscr):
        curses.curs_set(0)  # Skryje kurzor
        current_row = 0

        while True:
            stdscr.clear()
            height, width = stdscr.getmaxyx()

            # Vykreslení možností
            for idx, option in enumerate(options):
                x = 2
                y = idx + 2
                if idx == current_row:
                    stdscr.addstr(y, x, f"[x] {option}", curses.color_pair(1))
                else:
                    stdscr.addstr(y, x, f"[ ] {option}")

            # Aktualizace
            stdscr.refresh()

            # Čekání na vstup uživatele
            key = stdscr.getch()

            # Ovládání pomocí šipek
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(options) - 1:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter
                return options[current_row]

    return curses.wrapper(menu)


# Použití
options = ["První možnost", "Druhá možnost", "Třetí možnost"]
selected_option = select_with_arrows(options)
print(f"Vybrali jste: {selected_option}")
