import datetime
import tkinter as tk
from PIL import Image, ImageTk

#windowRes
window = tk.Tk()
window.geometry("440x520")
window.title("Age Calc")

#attributes
name = tk.Label(text = "Name")
name.grid(column=0,row=1)

name = tk.Label(text = "Year")
name.grid(column=0,row=2)

name = tk.Label(text = "Month")
name.grid(column=0,row=3)

name = tk.Label(text = "Day")
name.grid(column=0,row=4)

#Inputs
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)

yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)

monthEntry =  tk.Entry()
monthEntry.grid(column=1,row=3)

dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)

#fun
def getInput():
    name=nameEntry.get()
    user = Person(name,datetime.date(int(yearEntry.get()),
    int(monthEntry.get()),
    int(dateEntry.get())))

    textArea = tk.Text(master=window,height=15,width=25)
    textArea.gird(column=1, row=6)
    reply = "Hello {user}!, You're {age} years old.".format(user=name, age=user.age())
    textArea.insert(tk.End, reply)





window.mainloop()