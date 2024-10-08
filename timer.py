import time

def start_timer():
    global timer_seconds
    timer_seconds = 0
    update_timer()

def update_timer():
    global timer_seconds
    timer_seconds += 1
    timer_label.config(text=f"⏲   {timer_seconds // 60} : {timer_seconds % 60}")
    timer_label.after(1000, update_timer)

def pause_timer():
    global timer_paused
    timer_paused = True

def resume_timer():
    global timer_paused
    timer_paused = False
    update_timer()

