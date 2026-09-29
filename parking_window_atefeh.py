from tkinter import *
from parking_list import*

window = Tk()
window.title("parking")
window.geometry("500x500")


Label(window, text="name").place(x=20, y=20)
name = StringVar()
Entry(window, textvariable=name).place(x=120, y=20)

Label(window, text="color").place(x=20, y=60)
color = StringVar()
Entry(window, textvariable=color).place(x=120, y=60)

Label(window, text="plate").place(x=20, y=100)
plate = StringVar()
Entry(window, textvariable=plate).place(x=120, y=100)

Label(window, text="enter_time").place(x=20, y=140)
enter_time = StringVar()
Entry(window, textvariable=enter_time).place(x=120, y=140)


Button(window,text="Save").place(x=200, y=250, width=100)

window.mainloop()