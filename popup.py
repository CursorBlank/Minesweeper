import tkinter as tk

def flag_out_of_stock_popup(root):
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
    play_sound("./assets/audio/wrong.wav")
    label = tk.Label(
        popup, text="\U0001f6a9 \n Out of stock !", font=12, fg="White", bg="Black"
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

def open_unflag_popup(root, labels, rows, cols):
    popup = tk.Toplevel(root)
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
    play_sound("./assets/audio/wrong.wav")
    label = tk.Label(
        popup, text="Please unflag first !", font=12, fg="White", bg="Black"
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

def open_about_popup(root, labels, rows, cols):
    popup = tk.Toplevel(root)

    # Calculating the position to center the popup window with respect to the root window
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    popup_width = popup.winfo_reqwidth()
    popup_height = popup.winfo_reqheight()
    x = root_x + (root_width - popup_width) // 2
    y = root_y + (root_height - popup_height) // 2

    popup.geometry(f"+{x}+{y}")
    popup.configure(bg="#98FB98")
    popup.overrideredirect(True)  # Removes the Max, Min and Close buttons
    label = tk.Label(
        popup,
        text="\u00a9 \n 2024 \n MineSweeper 2.0 \n Author: DanveerKarna",
        font=12,
        fg="White",
        bg="Black",
    )
    label.pack(padx=20, pady=25)  # Way to give padding to the label

    close_button = tk.Button(
        popup,
        text="X",
        command=lambda rows=rows, cols=cols: close_about_popup(
            popup, labels, rows, cols
        ),
        font=12,
        fg="White",
        bg="Black",
    )
    close_button.pack(pady=15)

def close_about_popup(popup, labels, rows, cols):
    popup.destroy()
    mixer.music.stop()
    for r in range(rows):
        for c in range(cols):
            if labels[r][c].cget("state") != "disabled":
                play_sound_infinite("./assets/audio/music.ogg")

def close_gamewon_popup(popup, Name, rows, cols, mines):
    popup.destroy()
    mixer.music.stop()
    with open(
        "./data/csv/"
        + str(rows)
        + "x"
        + str(cols)
        + "_"
        + str(round(mines * (rows * cols) / 100))
        + ".csv",
        "a+",
    ) as History:
        History.write(
            Name
            + ","
            + timer_label.cget("text")[4 : len(timer_label.cget("text"))]
            .split(":")[0]
            .strip()
            + " m"
            + " "
            + timer_label.cget("text")[4 : len(timer_label.cget("text"))]
            .split(":")[1]
            .strip()
            + " s"
            + "\n"
        )

def close_popup(popup):
    popup.destroy()

def close_popup_with_music(popup):
    popup.destroy()
    mixer.music.stop()  # Stop playing the sound when the window is closed

def open_history_popup(root, rows, cols, mines):
    popup = tk.Toplevel(root)
    root_width = root.winfo_width()
    root_height = root.winfo_heightflag_out_of_stock_popup()
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    popup_width = popup.winfo_reqwidth()
    popup_height = popup.winfo_reqheight()
    x = root_x + (root_width - popup_width) // 2
    y = root_y + (root_height - popup_height) // 2

    popup.geometry(f"+{x}+{y}")
    popup.overrideredirect(True)
    play_sound("./assets/audio/winners.ogg")

    # Title = "\n#" + "   "+"Name\t\tTime\n"
    Display = "\n"
    Ranking = []
    try:
        with open(
            "./data/csv/"
            + str(rows)
            + "x"
            + str(cols)
            + "_"
            + str(round(mines * (rows * cols) / 100))
            + ".csv",
            "r",
        ) as History:
            content = History.readlines()
            for row in content:
                x = row.split(",")[1].strip().split(" m")[0]
                y = row.split(",")[1].strip().split(" m")[1].strip(" s")
                if x == "" and y != "":
                    s = 0 + int(row.split(",")[1].strip().split(" m")[1].strip(" s"))
                elif x != "" and y == "":
                    s = int(row.split(",")[1].strip().split(" m")[0]) * 60
                elif x == "" and y == "":
                    s = 0
                else:
                    s = int(row.split(",")[1].strip().split(" m")[0]) * 60 + int(
                        row.split(",")[1].strip().split(" m")[1].strip(" s")
                    )
                Ranking.append((s, row.split(",")[0].strip()))
            Ranking.sort()

            cnt = 0

            medals = ["\U0001f947", "\U0001f948", "\U0001f949"]
            for r in Ranking:
                if cnt > 2:
                    break
                Display += (
                    (
                        medals[cnt]
                        + "  "
                        + r[1]
                        + "  "
                        + (str(r[0] // 60) + "m ")
                        + str(r[0] % 60)
                        + "s"
                        + " "
                        + "\n"
                    )
                    if (int(str(r[0] // 60)) != 0)
                    else (
                        medals[cnt]
                        + "  "
                        + r[1]
                        + "  "
                        + str(r[0] % 60)
                        + "s"
                        + " "
                        + "\n"
                    )
                )
                cnt += 1
        label = tk.Label(
            popup, text=Display, font=2, bg="Black", fg="White", justify="left"
        )
    except:
        label = tk.Label(popup, text="No winners yet", font=16, bg="Black", fg="White")
    label.pack(padx=10, pady=5)

    close_button = tk.Button(
        popup,
        text="X",
        command=lambda: close_about_popup(popup, labels, rows, cols),
        font=12,
        fg="White",
        bg="Black",
    )
    close_button.pack(pady=5)

def custom_popup(init, root):
    popup = tk.Toplevel(root)
    popup.configure(bg="#98FB98")
    popup.overrideredirect(True)

    # Creating and positioning the input fields and labels
    tk.Label(popup, text="Height", font=("Helvetica", 12), bg="#98FB98").grid(
        row=0, column=0, padx=10, pady=5
    )
    rows_value = tk.StringVar()
    rows_value.set("8")  # Default value for rows
    rows_spinbox = tk.Spinbox(
        popup,
        from_=4,
        to=25,
        increment=1,
        width=10,
        font=("Helvetica", 12),
        textvariable=rows_value,
    )
    rows_spinbox.grid(row=1, column=0, padx=10, pady=5)

    tk.Label(popup, text="Width", font=("Helvetica", 12), bg="#98FB98").grid(
        row=2, column=0, padx=10, pady=5
    )
    cols_value = tk.StringVar()
    cols_value.set("8")  # Default value for columns
    cols_spinbox = tk.Spinbox(
        popup,
        from_=4,
        to=25,
        increment=1,
        width=10,
        font=("Helvetica", 12),
        textvariable=cols_value,
    )
    cols_spinbox.grid(row=3, column=0, padx=10, pady=5)

    tk.Label(popup, text="% Mines", font=("Helvetica", 12), bg="#98FB98").grid(
        row=4, column=0, padx=10, pady=5
    )
    mines_value = tk.StringVar()
    mines_value.set("16")  # Default value for mines
    mines_spinbox = tk.Spinbox(
        popup,
        from_=16,
        to=75,
        increment=1,
        width=10,
        font=("Helvetica", 12),
        textvariable=mines_value,
    )
    mines_spinbox.grid(row=5, column=0, padx=10, pady=5)

    # Creating and positioning the play button
    play_button = tk.Button(
        popup,
        text="\u25b6",
        command=lambda: level_custom(
            init,
            root,
            popup,
            int(rows_value.get()),
            int(cols_value.get()),
            int(mines_value.get()),
        ),
        font=("Helvetica", 12),
        bg="#FFD700",
        bd=2,
    )
    play_button.grid(row=6, column=0, padx=10, pady=5)

    close_button = tk.Button(
        popup,
        text="X",
        command=lambda: popup.destroy(),
        font=("Helvetica", 12),
        bg="Black",
        bd=2,
        fg="White",
    )
    close_button.grid(row=7, column=0, padx=10, pady=5)

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

    # Focusing on the mines Spinbox initially
    mines_spinbox.focus_set()

