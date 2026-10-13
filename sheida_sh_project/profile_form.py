from tkinter import *
from tkinter import messagebox

user_list = []


def save_click():
    try:
        user = {
            "mobile": mobile.get(),
            "national_code": national_code.get(),
            "card_number": card_number.get(),
            "plate": plate.get(),
            "bill_id": bill_id.get(),
        }
        user_list.append(user)
        # print(user_list)
        messagebox.showinfo(title="Saved", message="اطلاعات با موفقیت ثبت شد")

        mobile.set("")
        national_code.set("")
        card_number.set("")
        plate.set("")
        bill_id.set("")
    except Exception as e:
        messagebox.showerror(title="Save Error", message=f"خطا: {e}")

window = Tk()
window.title("Profile")
window.geometry("400x400")

# Mobile
Label(window, text="موبایل").place(x=20, y=20)
mobile = StringVar()
Entry(window, textvariable=mobile).place(x=120, y=20)

# National Code
Label(window, text="کد ملی").place(x=20, y=60)
national_code = StringVar()
Entry(window, textvariable=national_code).place(x=120, y=60)

# Card Number
Label(window, text="شماره کارت").place(x=20, y=100)
card_number = StringVar()
Entry(window, textvariable=card_number).place(x=120, y=100)

# Plate
Label(window, text="پلاک").place(x=20, y=140)
plate = StringVar()
Entry(window, textvariable=plate).place(x=120, y=140)

# Bill ID
Label(window, text="شناسه قبض").place(x=20, y=180)
bill_id = StringVar()
Entry(window, textvariable=bill_id).place(x=120, y=180)

Button(window, text="ثبت", command=save_click).place(x=150, y=280, width=80)

window.mainloop()