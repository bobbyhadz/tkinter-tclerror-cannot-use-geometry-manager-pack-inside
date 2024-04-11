# \_tkinter.TclError: cannot use geometry manager pack inside

from tkinter import Tk, ttk

root = Tk()

frm = ttk.Frame(root, padding=10)

frm.grid()

label = ttk.Label(frm, text="bobbyhadz.com")

# 👇️ Using grid()
label.grid(column=0, row=9)


button = ttk.Button(root, text="Quit",
                    command=root.destroy)

# 👇️ Using grid()
button.grid(column=1, row=0)


root.mainloop()