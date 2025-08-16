from tkinter import * # It is import * not import as Tk to make it more simple for example instead of Tk.label, here you write just label
from tkinter.ttk import Progressbar # Progress bar is part of ttk and not tkinter so you will have to do it separately
import psutil # Psutil

# Initialization of the Tkinter window
root = Tk()
# root.iconbitmap("") # Window Icon (Optional)
root.title("System Monitor") # Naming the title

# Functions
def updateusage(): # Function to update the progress bars
    CpuUsage = psutil.cpu_percent() #Fetch the Cpu Percentage from Psutil
    MemUsage = psutil.virtual_memory().percent #Fetch the Memory Percentage from Psutil
    DisUsage = psutil.disk_usage('/').percent # Fetch disk Usage from psutil
    CpuBar['value'] = CpuUsage # Configures the Progressbars to display the usage
    MemoryBar['value'] = MemUsage
    DiskBar['value'] = DisUsage
    root.after(1000, updateusage) # After 1 second it calls the function; thus refresshing the proggresbars
# Frame
TitleFrame = Frame(root)
TitleFrame.pack()

ActivityFrame = Frame(root)
ActivityFrame.pack()

UpdateFrame = Frame(root)
UpdateFrame.pack()
# Labels
TitleLabel = Label(TitleFrame, text= "Activity Monitor", font = "Arial 40 bold")
TitleLabel.grid(columnspan=2)

CpuLabel = Label(ActivityFrame, text= "Cpu Usage:",font="Arial 20")
CpuLabel.grid(column=0, row=0)
CpuBar = Progressbar(ActivityFrame, length=200)
CpuBar.grid(column=1,row=0)

MemoryLabel = Label(ActivityFrame, text = "Memory Usage:",font="Arial 20")
MemoryLabel.grid(column=0, row=1)
MemoryBar = Progressbar(ActivityFrame, length=200)
MemoryBar.grid(column=1,row=1)

DiskLabel = Label(ActivityFrame,text = "Disk Usage:",font="Arial 20")
DiskLabel.grid(column=0,row=2)
DiskBar = Progressbar(ActivityFrame, length=200)
DiskBar.grid(column=1,row=2)
updateusage()
root.mainloop()
