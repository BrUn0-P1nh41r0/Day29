import pyperclip
import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 9))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pw_filled = pw_entry.get()
    if pw_filled == "":
        pw_entry.insert(0, password)
        pyperclip.copy(password)
    else:
        pw_entry.delete(0,END)
        pw_entry.insert(0, password)
        pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    wb_get=wb_entry.get()
    eu_get=eu_entry.get()
    pw_get=pw_entry.get()
    new_data = {
        wb_get:{
            "email": eu_get,
            "password": pw_get
        }
    }

    if len(wb_get) == 0 or len(eu_get) == 0 or len(pw_get) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty! ")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode = "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                #Saving new data
                json.dump(data, data_file, indent=4)

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
gpw_button = Button(text="Generate Password", command=generate_password)
gpw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
