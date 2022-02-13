import datetime
import tkinter as tk
from PIL import Image, ImageTk

#window
window = tk.Tk()
window.geometry("540x720")
window.title("Age Calc")

#fields
name = tk.Label(text = "Name")
name.grid(column=0,row=1)

name = tk.Label(text = "Year")
name.grid(column=0,row=2)

name = tk.Label(text = "Month")
name.grid(column=0,row=3)

name = tk.Label(text = "Day")
name.grid(column=0,row=4)

#Entries
nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)

yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)

monthEntry =  tk.Entry()
monthEntry.grid(column=1,row=3)

dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)




window.mainloop()