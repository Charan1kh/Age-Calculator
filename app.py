import datetime
import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.geometry("540x720")
window.title("Age Calc")
name = tk.Label(text = "Name")
name.grid(column=0,row=1)

window.mainloop()