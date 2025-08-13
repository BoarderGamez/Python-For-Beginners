from tkinter import *

root = Tk()
root.iconbitmap("Tomato.ico")
root.title("Pomodoro Timer")


# Function

def timer(time):
    global Stop
    if time >= 0:
        mins = time // 60
        secs = time % 60
        TimerLabel.config(text=f"{mins}:{secs}")
        if not Stop:
            root.after(1000, timer, time - 1)
        else:
            Stop = False
            TimerLabel.config(text="00:00")
            return

    else:
        TimerLabel.config(text="00:00")


def stop():
    global Stop
    Stop = True


# Variables
Stop = False
# Frames
TimerFrame = Frame(root)
TimerFrame.pack(padx=10, pady=10)

ButtonFrame = Frame(root)
ButtonFrame.pack(padx=10, pady=10)

# Labels
TimerLabel = Label(TimerFrame, text="00:00", font=("Arial", 40, "bold"))
TimerLabel.grid(column=0, columnspan=3, padx=20, pady=20)

# Buttons
StartButton = Button(ButtonFrame, text="Start", font=(
    "Arial", 15), bg="Light Green", command=lambda: timer(1500))
StartButton.grid(column=0, row=0, padx=5)

StopButton = Button(ButtonFrame, text="Reset", font=(
    "Arial", 15), bg="Red", command=stop)
StopButton.grid(column=3, row=0, padx=5)

SmallBreakButton = Button(ButtonFrame, text="Small Break", font=(
    "Arial", 15), bg="Light Blue", command=lambda: timer(300))
SmallBreakButton.grid(column=1, row=0, padx=5)

BigBreakButton = Button(ButtonFrame, text="Big Break", font=(
    "Arial", 15), bg="Orange", command=lambda: timer(900))
BigBreakButton.grid(column=2, row=0, padx=5)
root.mainloop()
