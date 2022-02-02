from tkinter import *
import math

# What if, on line 65, there was a function that passed a True/False modifier on some variable.
# The countdown function would need an 'If True' conditional
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
run_timer = True
count = 0


def main():
    # Needs to have pause functionality added
    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer():
        window.after_cancel(timer)
        timer_label.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text="00:00")
        check_mark.config(text="")
        global reps
        reps = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    def start_timer():
        global reps
        reps += 1

        if reps % 2 == 1:
            timer_label.config(text="Work", fg=RED)
            count_down(WORK_MIN * 60)
            window.attributes("-topmost", True)
            window.attributes("-topmost", False)
        elif reps % 8 == 0:
            timer_label.config(text="Break", fg=GREEN)
            count_down(LONG_BREAK_MIN * 60)
            window.attributes("-topmost", True)
            window.attributes("-topmost", False)
        else:
            timer_label.config(text="Break", fg=PINK)
            count_down(SHORT_BREAK_MIN * 60)
            window.attributes("-topmost", True)
            window.attributes("-topmost", False)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(time_count):
        global run_timer
        global count
        count = time_count
        start_button.config(text="Pause", command=pause_timer)

        count_min = math.floor(count / 60)
        count_sec = (count % 60)
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            if run_timer:
                global timer
                timer = window.after(1000, count_down, count - 1)
            else:
                start_button.config(text="Start")
        else:
            start_timer()
            checks = ""
            work_sessions = math.floor(reps/2)
            for i in range(work_sessions):
                if reps % 2 == 0:
                    checks += "✔"
                    check_mark.config(text=checks)

    def pause_timer():
        global run_timer
        if run_timer:
            run_timer = False
        else:
            run_timer = True
            count_down(count)


    # ---------------------------- UI SETUP ------------------------------- #

    window = Tk()
    window.title("Pomodoro Timer")
    window.config(padx=100, pady=50, bg=YELLOW)

    timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    timer_label.grid(column=1, row=0)

    start_button = Button(text="Start", width=7, command=start_timer, highlightthickness=0)
    start_button.grid(column=0, row=2)

    reset_button = Button(text="Reset", width=7, command=reset_timer, highlightthickness=0)
    reset_button.grid(column=2, row=2)

    check_mark = Label(fg=GREEN, bg=YELLOW)
    check_mark.grid(column=1, row=3)

    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tom_pic = PhotoImage(file="tomato.png")
    canvas.create_image(100, 112, image=tom_pic)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=1, row=1)

    window.mainloop()


if __name__ == '__main__':
    main()
