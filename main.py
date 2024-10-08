import numpy as np
import tkinter as tk
from timer import start_timer, update_timer, pause_timer, resume_timer
from game_logic import create_grid, button_click, on_right_click, check_game_won, open_gameover_popup, open_gamewon_popup
from popup import flag_out_of_stock_popup, open_unflag_popup, open_about_popup, close_about_popup, close_gamewon_popup, close_popup, close_popup_with_music, open_history_popup, custom_popup
from audio import play_sound, play_sound_nonzero, play_sound_zero, play_sound_infinite
from levels import level8, level16, level24, level_custom, new

def initialize(root, BtnSize=31, rows=8, cols=8, mines=16):
    global timer_label
    global timer_started, timer_paused
    global first_click
    # Initialize timer label
    timer_started = False
    timer_paused = False
    timer_seconds = 0
    timer_label = None
    first_click = True
    global cnt, BUTTON_SIZE, flagged, visited, btnVal, labels

    BUTTON_SIZE = BtnSize
    cnt = 0
    flagged = []
    visited = []
    btnVal = []
    labels = []

    timer_label = tk.Label(root, text="⏲   0 : 0", bg="Black", fg="Red", padx=20)
    timer_label.grid(row=0, column=0, columnspan=cols)

    arr = np.zeros([rows, cols])
    create_grid(root, arr, labels, cnt, flagged, visited, btnVal, mines, rows, cols)
    play_sound_infinite("./assets/audio/music.ogg")

    load(rows, cols, mines)

def load(rows, cols, mines):
    # Creating a menu bar
    menubar = tk.Menu(root)

    # Getting the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Getting the root window width and height
    root_width = root.winfo_reqwidth()
    root_height = root.winfo_reqheight()

    # Calculating the positioning to center the root window
    x = (screen_width - root_width) // 2
    y = (screen_height - root_height) // 2

    # Setting the root window position
    root.geometry(f"+{x}+{y}")

    # Creating File menu
    file_menu = tk.Menu(menubar, tearoff=0)
    # Creating Sub-menu under Level menu
    sub_menu = tk.Menu(file_menu, tearoff=False)
    file_menu.add_command(
        label="\U0001f501 Replay",
        command=lambda rows=rows, cols=cols, mines=mines: new(
            initialize, root, rows, cols, mines
        ),
    )
    sub_menu.add_command(
        label="\U0001f530 Beginner", command=lambda: level8(initialize, root)
    )
    sub_menu.add_command(
        label="\U00002b50 Intermediate", command=lambda: level16(initialize, root)
    )
    sub_menu.add_command(
        label="\U0001f525 Expert", command=lambda: level24(initialize, root)
    )
    sub_menu.add_separator()
    sub_menu.add_command(
        label="🛠️ Custom", command=lambda: custom_popup(initialize, root)
    )
    file_menu.add_cascade(label="\U0001fa9c Level", menu=sub_menu)
    file_menu.add_command(
        label="\U0001f3c6 Winners",
        command=lambda rows=rows, cols=cols, mines=mines: open_history_popup(
            root, rows, cols, mines
        ),
    )
    file_menu.add_command(
        label="\U0001f4dc About",
        command=lambda rows=rows, cols=cols, mines=mines: open_about_popup(
            root, labels, rows, cols
        ),
    )
    file_menu.add_separator()
    file_menu.add_command(
        label="\U0001f6aa Exit", command=lambda labels=labels: root.destroy()
    )
    menubar.add_cascade(label=" \u2630 ", menu=file_menu)
    root.resizable(False, False)  # Horizontal, Vertical both set to false
    root.title("🎮 MineSweeper")
    root.config(menu=menubar)

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    initialize(root)

