import sqlite3
from tkinter import *
from PIL import Image, ImageTk
import pathlib, os

# controllers
def get_asset(img_file_name):
    curr_dir = pathlib.Path(__file__).parent.resolve()
    img_path = os.path.join(curr_dir, "assets", img_file_name)
    return img_path

def create_account():
    # input user creation here
    user_found = False # temp signup
    if user_found:
        # alert: username already exist
        print("Impostor")
    else:
        # alert: user created
        open_login

def open_login():
    signup_window.destroy()
    import gui_login
    gui_login.main()

# colors
color_black = "#323232"
color_lightgray = "#D9D9D9"
color_gray = "#9F9F9F"
color_lightblue = "#A5ABE2"
color_blue = "#6D79E2"
color_lightred = "#DE8E8E"
color_red = "#ED4D4D"

# window resolutions
reso_login = '300x400'
reso_home = '750x500'

# root window
signup_window = Tk()
signup_window.title(' ')
signup_window.geometry(reso_login)
signup_window.configure(bg = color_lightgray)
signup_window.resizable(False,False)

# assets
img_icon = Image.open(get_asset("logo.png"))
res_icon = img_icon.resize((32,32), resample = 3)
icon = ImageTk.PhotoImage(res_icon)

img_confirm = Image.open(get_asset("confirm.png"))
res_confirm = img_confirm.resize((45,45), resample = 3)
confirm = ImageTk.PhotoImage(res_confirm)

img_back = Image.open(get_asset("back.png"))
res_back = img_back.resize((45,45), resample = 3)
back = ImageTk.PhotoImage(res_back)

# header
Frame(signup_window, width = 300, height = 60, bg = color_blue).place(x=0,y=0)
Label(image = icon, bg = color_blue).place(x=134,y=14)

# login container
frame = Frame(signup_window, width = 250, height = 285, bg = color_lightgray)
# frame = Frame(signup_window, width = 250, height = 285, bg = "red")
frame.place(x=25,y=90)

usertext = Label(frame, text = 'username', fg = color_black, bg = color_lightgray, font = ("Ubuntu Mono", 14))
usertext.place(x=0,y=70+10)
passtext = Label(frame, text = 'password', fg = color_black, bg = color_lightgray, font = ("Ubuntu Mono", 14))
passtext.place(x=0,y=145+10)

userbox = Entry(frame, width = 25, fg = color_black, bg = color_lightgray, border = 0, font = ("Ubuntu Mono", 16, "bold"))
userbox.place(x=0,y=95+10)
passbox = Entry(frame, width = 25, fg = color_black, bg = color_lightgray, border = 0, font = ("Ubuntu Mono", 16, "bold"), show = "*")
passbox.place(x=0,y=170+10)

Frame(frame,width = 250, height = 1, bg = color_black).place(x=0,y=121+10)
Frame(frame,width = 250, height = 1, bg = color_black).place(x=0,y=196+10)

Button(frame, image = back, bg = color_lightgray, borderwidth = 0, highlightthickness = 0, relief = "flat", command = open_login).place(x=5,y=5)
Button(frame, image = confirm, bg = color_lightgray, borderwidth = 0, highlightthickness = 0, relief = "flat", command = open_login).place(x=200,y=175+60)

signup_window.mainloop()