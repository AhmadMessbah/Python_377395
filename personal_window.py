from tkinter import *

window = Tk()
window.title("student info")
window.geometry("500x500")

Label(window, text="name").place(x=20, y=20)
name = StringVar()
Entry(window, textvariable=name).place(x=120, y=20)

Label(window, text="family").place(x=20, y=60)
family = StringVar()
Entry(window, textvariable=family).place(x=120, y=60)

Label(window, text="age").place(x=20, y=100)
age = StringVar()
Entry(window, textvariable=age).place(x=120, y=100)

Label(window, text="birth year").place(x=20, y=140)
year = StringVar()
Entry(window, textvariable=year).place(x=120, y=140)

Label(window, text="birth month").place(x=20, y=180)
month = StringVar()
Entry(window, textvariable=month).place(x=120, y=180)

Label(window, text="birth day").place(x=20, y=220)
day = StringVar()
Entry(window, textvariable=day).place(x=120, y=220)

Button(window,text="Save").place(x=200, y=250, width=100)

window.mainloop()