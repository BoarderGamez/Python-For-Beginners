from tkinter import * # It is import * not import as Tk to make it more simple for example instead of Tk.label, here you write just label
from tkinter.ttk import Progressbar
import psutil

# Initialization of the Tkinter window
root = Tk()
# root.iconbitmap("") # Window Icon (Optional)
root.title("System Monitor") # Naming the title

# Functions
def updateusage(): # Function to update the progress bars
    CpuUsage = psutil.cpu_percent() #Fetch the Cpu Percentagefrom Psutil
    MemUsage = psutil.virtual_memory().percent #F
    DisUsage = psutil.disk_usage('/').percent
    CpuBar['value'] = CpuUsage
    MemoryBar['value'] = MemUsage
    DiskBar['value'] = DisUsage
    root.after(1000, updateusage)
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
