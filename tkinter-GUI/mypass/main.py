from tkinter import *
from tkinter.messagebox import showinfo, showerror
import random
import json

WINDOW_WIDTH = 250
WINDOW_HEIGHT = 250
IMG = "tkinter-GUI/mypass/img.png"
IMG_WIDTH = 218
IMG_HEIGHT = 207
BACKGROUND_COLOR = "white"
MY_EMAIL = "user@gmail.com"
DATA_FILE = "tkinter-GUI/mypass/passwords.txt"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
C_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#####----------------------------- Setup Screen Widgets -----------------------------#####
window = Tk()
window.title("Password Mannager")
window.config(padx=50, pady=50, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR)

canvas = Canvas(width=IMG_WIDTH, height=IMG_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
img = PhotoImage(file=IMG)
canvas.create_image(IMG_WIDTH/2, IMG_HEIGHT/2, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg=BACKGROUND_COLOR)
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", bg=BACKGROUND_COLOR)
username_label.grid(row=2, column=0)
username_label.config(padx=5)

password_label = Label(text="Password:", bg=BACKGROUND_COLOR)
password_label.grid(row=3, column=0)

website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2, sticky=W)
website_entry.focus()

username_entry = Entry(width=55)
username_entry.grid(row=2, column=1, columnspan=2, sticky=W)
username_entry.insert(END, MY_EMAIL)

password_entry = Entry(width=36)
password_entry.grid(row=3, column=1, sticky=W)

#####----------------------------- Screen Functionality -----------------------------#####
def generate_password():
    """
    Generates a new valid password.
    A valid password contains letters, capital letters, numbers, and symbols - two of each.
    """
    password_list = []

    for _ in range(2):
        password_list.append(random.choice(LETTERS))
        password_list.append(random.choice(C_LETTERS))
        password_list.append(random.choice(SYMBOLS))
        password_list.append(random.choice(NUMBERS))

    random.shuffle(password_list)
    password = "".join(password_list)

    # fill in the entry with the generated password.
    password_entry.insert(0, password)

def add_website():
    """Updates 'passwords.txt' file with the new website and password."""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_json_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == "" or username == "" or password == "":
        # inform the user that some information is missing.
        showinfo(title="Missing Info", message="Some fields are empty. \nNothing was save.")

    else:
        try:
            # try to open 'data.json'
            with open("tkinter-GUI/mypass/data.json") as json_file:
                # read old data
                data_dict = json.load(json_file)
        except FileNotFoundError:
            # if file not exist then create it
            with open("tkinter-GUI/mypass/data.json", "w") as json_file:
                json.dump(new_json_data, json_file, indent=4)
        else:
            # if file exist then update old data with new data

            if website not in data_dict:
                # if this website does not exist yet in the passwords file then add it
                data_dict.update(new_json_data)
                showinfo(title="Information", message="The password added successfully to your passwords file.")
            else:
                # update the password of the existing website
                data_dict[website]["password"] = password
                showinfo(title="Update", message="New password updated for the existing website.")

            with open("tkinter-GUI/mypass/data.json", "w") as json_file:
                # save updated data
                json.dump(data_dict, json_file, indent=4)
        finally:
            with open(DATA_FILE, "a") as txt_file:
                txt_file.write(f"{website} | {username} | {password}\n")
            
            # clear the entries on the screen.
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    """Search info of the current website, and show it on screen."""
    try:
        # try to open 'data.json'
        with open("tkinter-GUI/mypass/data.json") as json_file:
            data_dict = json.load(json_file)
    except FileNotFoundError:
        # if file not exist then let the user know
        showerror(title="Error", message="Your passwords file does not exist yet.")
    else:
        website = website_entry.get()
        if website in data_dict:
            username = data_dict[website]["username"]
            password = data_dict[website]["password"]

            username_entry.delete(0, END)
            username_entry.insert(0, username)
            password_entry.delete(0, END)
            password_entry.insert(0, password)
        else:
            showerror(title="Error", message="{website} does not exist in your passwords file.")
            


gen_pass_btn = Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(row=3, column=2, sticky=W)

add_btn = Button(text="Add", command=add_website, width=46)
add_btn.grid(row=4, column=1, columnspan=2, sticky=W)

search_btn = Button(text="Search", command=search, width=14)
search_btn.grid(row=1, column=2)



window.mainloop()