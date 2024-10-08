import numpy as np
import tkinter as tk

def create_grid(root, bombs, labels, cnt, flagged, visited, btnVal, should_be_disabled=False, rows=8, cols=8, mines=16):
    for row in range(rows):
        label_row = []  # List to store labels in each row
        for col in range(cols):
            label = tk.Label(root, text="", width=31, height=31)#=BUTTON_SIZE
            label.grid(row=row + 1, column=col)
            label_row.append(label)
        labels.append(label_row)

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        flagged.append(row)
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        btnVal.append(row)
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        visited.append(row)

    for r in range(rows):
        for c in range(cols):
            labels[r][c].bind(
                "<Button-1>",
                lambda event, visited=visited, row=r, col=c: button_click(
                    root,
                    bombs,
                    cnt,
                    visited,
                    btnVal,
                    labels,
                    row,
                    col,
                    flagged,
                    should_be_disabled,
                    rows,
                    cols,
                    mines,
                ),
            )
            labels[r][c].bind(
                "<Button-3>",
                lambda event,
                btnVal=btnVal,
                labels=labels,
                row=r,
                col=c,
                flagged=flagged,
                should_be_disabled=should_be_disabled: on_right_click(
                    root,
                    btnVal,
                    labels,
                    row,
                    col,
                    flagged,
                    should_be_disabled,
                    rows,
                    cols,
                    mines,
                ),
            )
            # Setting background images based on the btnVal
            image_filename = "./assets/imgs/btn.png"

            # Setting background image for the label
            img = tk.PhotoImage(file=image_filename)
            labels[r][c].config(image=img)
            labels[r][c].image = img  # Keeping a reference to the image to prevent garbage collection

    return

def button_click(
    root,
    bombs,
    cnt,
    visited,
    btnVal,
    labels,
    row,
    col,
    flagged,
    should_be_disabled,
    rows=8,
    cols=8,
    mines=16,
):
    global timer_started
    global first_click

    if not timer_started:
        start_timer()
        timer_started = True
    if first_click:
        first_click = False
        store = []
        while len(store) != round(mines * (rows * cols) / 100):
            x, y = generate_random_tuple(rows, cols)
            if (x, y) not in store and (x - 1, y - 1) != (row, col):
                store.append((x, y))
        for x, y in store:
            bombs[x - 1, y - 1] = 1

        for r in range(rows):
            for c in range(cols):
                if bombs[r][c] == 1:
                    btnVal[r][c] = "*"

        for r in range(rows):
            for c in range(cols):
                if btnVal[r][c] != "*":
                    if c - 1 >= 0:
                        if btnVal[r][c - 1] == "*":
                            btnVal[r][c] += 1
                    if c + 1 < cols:
                        if btnVal[r][c + 1] == "*":
                            btnVal[r][c] += 1
                    if r - 1 >= 0:
                        if btnVal[r - 1][c] == "*":
                            btnVal[r][c] += 1
                        if c - 1 >= 0:
                            if btnVal[r - 1][c - 1] == "*":
                                btnVal[r][c] += 1
                        if c + 1 < cols:
                            if btnVal[r - 1][c + 1] == "*":
                                btnVal[r][c] += 1
                    if r + 1 < rows:
                        if btnVal[r + 1][c] == "*":
                            btnVal[r][c] += 1
                        if c - 1 >= 0:
                            if btnVal[r + 1][c - 1] == "*":
                                btnVal[r][c] += 1
                        if c + 1 < cols:
                            if btnVal[r + 1][c + 1] == "*":
                                btnVal[r][c] += 1

    if flagged[row][col] != 0:
        if visited[row][col] == 1:
            pass
        else:
            open_unflag_popup(root, labels, rows, cols)
    else:
        if btnVal[row][col] == "*" and visited[row][col] == 0:
            for r in range(rows):
                for c in range(cols):
                    if btnVal[r][c] == "*":
                        if flagged[r][c] == 1:
                            image_filename = "./assets/imgs/bomb_flag.png"

                            img = tk.PhotoImage(file=image_filename)
                            labels[r][c].config(image=img)
                            labels[r][c].image = img
                        else:
                            image_filename = "./assets/imgs/bomb.png"

                            img = tk.PhotoImage(file=image_filename)
                            labels[r][c].config(image=img)
                            labels[r][c].image = img
                        image_filename = "./assets/imgs/blasted_bomb.png"

                        img = tk.PhotoImage(file=image_filename)
                        labels[row][col].config(image=img)
                        labels[row][col].image = img
                    visited[r][c] = 1
            pause_timer()
            should_be_disabled = True
            open_gameover_popup(root)

        elif btnVal[row][col] == 0 and visited[row][col] == 0:
            play_sound_zero("./assets/audio/unlock.mp3")
            # Setting background image for the label
            img = tk.PhotoImage(file="./assets/imgs/brown.png")
            labels[row][col].config(image=img)

            labels[row][
                col
            ].image = (
                img  # Keeping a reference to the image to prevent garbage collection
            )

            visited[row][col] = 1

            open_help(
                cnt, visited, btnVal, labels, row, col, flagged, rows, cols, mines
            )
        elif btnVal[row][col] not in ["*", 0] and visited[row][col] == 0:
            play_sound_nonzero("./assets/audio/click.wav")
            image_filename = "./assets/imgs/" + str(btnVal[row][col]) + ".png"
            # Setting background image for the label
            img = tk.PhotoImage(file=image_filename)
            labels[row][col].config(image=img)

            labels[row][
                col
            ].image = (
                img  # Keeping a reference to the image to prevent garbage collection
            )

            visited[row][col] = 1

    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == 1:
                cnt += 1
    if (rows * cols) - cnt == round(mines * (rows * cols) / 100):
        for r in range(rows):
            for c in range(cols):
                if btnVal[r][c] == "*":
                    if flagged[r][c] == 1:
                        image_filename = "./assets/imgs/bomb_flag.png"

                        img = tk.PhotoImage(file=image_filename)
                        labels[r][c].config(image=img)
                        labels[r][c].image = img
                    else:
                        image_filename = "./assets/imgs/bomb.png"

                        img = tk.PhotoImage(file=image_filename)
                        labels[r][c].config(image=img)
                        labels[r][c].image = img

                visited[r][c] = 1
        pause_timer()
        should_be_disabled = True
        open_gamewon_popup(root, rows, cols, mines)


def on_right_click(
    root,
    btnVal,
    labels,
    row,
    col,
    flagged,
    should_be_disabled,
    rows=8,
    cols=8,
    mines=16,
):
    flag_cnt = 0

    if should_be_disabled:
        if visited[row][col] == 0 and flagged[row][col] != 0:
            image_filename = "./assets/imgs/btn.png"
            img = tk.PhotoImage(file=image_filename)
            labels[row][col].config(image=img)
            labels[row][
                col
            ].image = img  # Keeping a reference to the image to prevent garbage collection, without this image is not being displayed
            play_sound("./assets/audio/unflag.wav")
            flagged[row][col] = 0

        elif visited[row][col] == 0 and flagged[row][col] == 0:
            for r in range(rows):
                for c in range(cols):
                    if flagged[r][c] == 1:
                        flag_cnt += 1
                    if flag_cnt == round(mines * (rows * cols) / 100):
                        flag_out_of_stock_popup(root)
                        return

            image_filename = "./assets/imgs/flag.png"
            img = tk.PhotoImage(file=image_filename)
            labels[row][col].config(image=img)
            labels[row][col].image = img
            play_sound("./assets/audio/flag.wav")
            flagged[row][col] = 1


def check_game_won():
    # Logic to check if the game has been won
    pass

def open_gameover_popup(root):
    popup = tk.Toplevel(root)

    # Calculating the positioning to center the popup window with respect to the root window
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    popup_width = popup.winfo_reqwidth()
    popup_height = popup.winfo_reqheight()
    x = root_x + (root_width - popup_width) // 2
    y = root_y + (root_height - popup_height) // 2

    popup.geometry(f"+{x}+{y}")
    popup.configure(bg="#FF2400")
    popup.overrideredirect(True)
    play_sound("./assets/audio/gameOver.wav")
    label = tk.Label(
        popup, text="\U0001f480 \n Game over !", font=12, fg="White", bg="Black"
    )
    label.pack(padx=20, pady=25)

    close_button = tk.Button(
        popup,
        text="X",
        command=lambda: close_popup_with_music(popup),
        font=12,
        fg="White",
        bg="Black",
    )
    close_button.pack(pady=15)


def open_gamewon_popup(root, rows, cols, mines):
    popup = tk.Toplevel(root)

    # Calculating the positioning to center the popup window with respect to the root window
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    popup_width = popup.winfo_reqwidth()
    popup_height = popup.winfo_reqheight()
    x = root_x + (root_width - popup_width) // 2
    y = root_y + (root_height - popup_height) // 2

    popup.geometry(f"+{x}+{y}")
    popup.configure(bg="#32CD32")
    popup.overrideredirect(True)
    play_sound("./assets/audio/gameWin.wav")

    label = tk.Label(
        popup,
        text=timer_label.cget("text") + "\n 🏆 \n You won !",
        font=12,
        fg="White",
        bg="#FF8C00",
    )
    label.pack(padx=20, pady=25)
    Name = tk.Entry(popup)
    Name.pack(pady=15)
    close_button = tk.Button(
        popup,
        text="X",
        command=lambda: close_gamewon_popup(popup, Name.get(), rows, cols, mines),
        font=12,
        fg="White",
        bg="#FF8C00",
    )
    close_button.pack(pady=15)

