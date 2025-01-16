from random import lognormvariate
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#Image
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,110, image=logo_img)
canvas.grid(column = 1, row= 0)

#Labels
wb_label = Label(text="Website:")
wb_label.grid(column=0, row=1)

eu_label= Label(text="Email/Username:")
eu_label.grid(column=0, row=2)

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

#Entry
wb_entry = Entry(width=35)
wb_entry.grid(column=1, row=1, columnspan=2)

eu_entry = Entry(width=35)
eu_entry.grid(column=1, row=2, columnspan=2)

eu_entry = Entry(width=21)
eu_entry.grid(column=1, row=3)


#Buttons
gpw_button = Button(text="Generate Password")
gpw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
