from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    wb_get=wb_entry.get()
    eu_get=eu_entry.get()
    pw_get=pw_entry.get()

    if len(wb_get) == 0 or len(eu_get) == 0 or len(pw_get) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty! ")
    else:
        is_ok = messagebox.askokcancel(title=wb_get, message=f"These are the details entered: \nEmail: {eu_get}"
                                                             f"\nPassword: {pw_get} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_filed:
                data_filed.write(f"{wb_get} | {eu_get} | {pw_get}\n")
            clear_data()

def clear_data():
    wb_entry.delete(0,END)
    eu_entry.delete(0,END)
    eu_entry.insert(0, "bpinheiro@live.com.pt")
    pw_entry.delete(0,END)


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
wb_entry.focus()

eu_entry = Entry(width=35)
eu_entry.grid(column=1, row=2, columnspan=2)
eu_entry.insert(0, "bpinheiro@live.com.pt")

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)


#Buttons
gpw_button = Button(text="Generate Password")
gpw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
