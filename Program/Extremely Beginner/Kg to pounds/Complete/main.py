from tkinter import * # It is import * not import as Tk to make it more simple for example instead of Tk.label, here you write just label
root =Tk()

def Convert(): # When the button is pressed this function runs
    Kgs = KgTextVar.get() # Fetch the value from the Kg entry
    Converted = Kgs*2.20462262 # Convert to pounds
    Lb.delete(0, END) # Clear the pound entry
    Lb.insert(0, Converted) # Insert the new value

KgTextVar = IntVar() # The textvariables for both entries
LbTextVar = IntVar()
# Elements
Kg=Entry(root, textvariable=KgTextVar)
Kg.grid(row=0,column=0,pady=10,padx=10)

Lb=Entry(root, textvariable=LbTextVar)
Lb.grid(row=0,column=2,pady=10,padx=10)

ConvertLabel = Label(root, text="Kg to Lb")
ConvertLabel.grid(row=0,column=1,pady=10,padx=10)

ConvertButton = Button(root,text="Convert",command = Convert)
ConvertButton.grid(row=1,column=1,pady=10,padx=10)

root.mainloop()