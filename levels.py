def level8(init, root):
    timer_label.destroy()
    for widget in root.grid_slaves():
        widget.grid_forget()
    init(root, 31, 8, 8)

def level16(init, root):
    timer_label.destroy()
    for widget in root.grid_slaves():
        widget.grid_forget()
    init(root, 31, 16, 16)

def level24(init, root):
    timer_label.destroy()
    for widget in root.grid_slaves():
        widget.grid_forget()
    init(root, 31, 24, 24)

def level_custom(init, root, popup, rows, cols, mines):
    close_popup(popup)
    timer_label.destroy()
    for widget in root.grid_slaves():
        widget.grid_forget()
    init(root, 31, rows, cols, mines)
    
def new(init, root, rows, cols, mines):
    timer_label.destroy()
    for widget in root.grid_slaves():
        widget.grid_forget()
    init(root, 31, rows, cols, mines)

