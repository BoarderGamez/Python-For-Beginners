from tkinter import * # It is import * not import as Tk to make it more simple for example instead of Tk.label, here you write just label

# Initialization of the Tkinter window
root = Tk()
root.iconbitmap("Tomato.ico") # Window Icon
root.title("Pomodoro Timer") # Naming the title

# Functions
def timer(time):
    global Stop # You require this because of line 18, without this it would be thought that the Stop variable is local.
    if time >= 0: # While the timer is running
        mins = time // 60
        secs = time % 60
        TimerLabel.config(text=f"{mins}:{secs}") # Config, to change the timer
        if not Stop: # If the stop button has not been pressed.
            root.after(1000, timer, time - 1) # After 1000ms (1s) run timer again and count down a second
        else: # If stop has been set to true
            Stop = False # Set the stop variable to false
            TimerLabel.config(text="00:00") # Reset the timer
            return # Exit the function

    else: # If the timer is done, reset the clock
        TimerLabel.config(text="00:00")

# Function For Stop Button
def stop(): # This happens when the stop button is pressed
    global Stop
    Stop = True


# Variables
Stop = False
# Frames
TimerFrame = Frame(root) # Optional, but frames can make it easier to organize your program
TimerFrame.pack(padx=10, pady=10)

ButtonFrame = Frame(root) # Optional, but frames can make it easier to organize your program
ButtonFrame.pack(padx=10, pady=10)

# Labels
TimerLabel = Label(TimerFrame, text="00:00", font=("Arial", 40, "bold"))
TimerLabel.grid(column=0, columnspan=4, padx=20, pady=20) # Columnspan is to stretch it across that many columns

# Buttons
StartButton = Button(ButtonFrame, text="Start", font=(
    "Arial", 15), bg="Light Green", command=lambda: timer(1500)) # Lambda is there so that a function with a parameter can be used without calling the function
StartButton.grid(column=0, row=0, padx=5)

StopButton = Button(ButtonFrame, text="Reset", font=(
    "Arial", 15), bg="Red", command=stop)
StopButton.grid(column=3, row=0, padx=5)

SmallBreakButton = Button(ButtonFrame, text="Small Break", font=(
    "Arial", 15), bg="Light Blue", command=lambda: timer(300)) # Lambda is there so that a function with a parameter can be used without calling the function
SmallBreakButton.grid(column=1, row=0, padx=5)

BigBreakButton = Button(ButtonFrame, text="Big Break", font=(
    "Arial", 15), bg="Orange", command=lambda: timer(900)) # Lambda is there so that a function with a parameter can be used without calling the function
BigBreakButton.grid(column=2, row=0, padx=5)

root.mainloop()
