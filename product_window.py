from tkinter import *
from store_module import*

window = Tk()
window.title("product")
window.geometry("500x500")


Label(window, text="name").place(x=20, y=20)
name= StringVar()
Entry(window, textvariable=name ).place(x=120, y=20)

Label(window, text="quantity").place(x=20, y=60)
quantity= StringVar()
Entry(window, textvariable=quantity).place(x=120, y=60)

Label(window, text="price").place(x=20, y=100)
price= StringVar()
Entry(window, textvariable=price).place(x=120, y=100)

Label(window, text="description").place(x=20, y=140)
description= StringVar()
Entry(window, textvariable=description).place(x=120, y=140)


Button(window,text="Save").place(x=200, y=250, width=100)

window.mainloop()