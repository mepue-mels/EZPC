"""gui_login.py"""

import sqlite3
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pathlib, os
from ezpc_functions import *

def main():
    
    # controllers
    def get_asset(img_file_name):
        curr_dir = pathlib.Path(__file__).parent.resolve()
        img_path = os.path.join(curr_dir, "assets", img_file_name)
        return img_path

    def verify():
        # print(userbox.get() + " " + passbox.get())
        # user_found = False # temp login
        user = login_user(userbox.get(),passbox.get())
        if user:
            open_ezpc(user)
        else:
            # alert: Invalid username / password
            print("Thou shall not pass!")
            userbox.delete(0, END)
            passbox.delete(0, END)
            messagebox.showerror(title="Thou shall not pass!", message="Invalid credentials.")

    def open_ezpc(user):
        print(user)
        pc = user.new_pc()
        login_window.destroy()
        import gui_home
        gui_home.main(user, pc)
        # menu_main(user)

    def open_signup():
        login_window.destroy()
        import gui_signup
        gui_signup.main()

    

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
    login_window = Tk()
    login_window.title(' ')
    login_window.geometry(reso_login)
    login_window.configure(bg = color_lightgray)
    login_window.resizable(False,False)

    # assets
    img_icon = Image.open(get_asset("logo.png"))
    res_icon = img_icon.resize((64,64), resample = 3)
    icon = ImageTk.PhotoImage(res_icon)

    img_enter = Image.open(get_asset("enter.png"))
    res_enter = img_enter.resize((45,45), resample = 3)
    enter = ImageTk.PhotoImage(res_enter)

    # header
    Frame(login_window, width = 300, height = 120, bg = color_blue).place(x=0,y=0)
    Label(image = icon, bg = color_blue).place(x=118,y=28)

    # login container
    frame = Frame(login_window, width = 250, height = 225, bg = color_lightgray)
    frame.place(x=25,y=150)

    usertext = Label(frame, text = 'username', fg = color_black, bg = color_lightgray, font = ("Ubuntu Mono", 14))
    usertext.place(x=0,y=0+10)
    passtext = Label(frame, text = 'password', fg = color_black, bg = color_lightgray, font = ("Ubuntu Mono", 14))
    passtext.place(x=0,y=75+10)

    userbox = Entry(frame, width = 25, fg = color_black, bg = color_lightgray, border = 0, font = ("Ubuntu Mono", 16, "bold"))
    userbox.place(x=0,y=25+10)
    passbox = Entry(frame, width = 25, fg = color_black, bg = color_lightgray, border = 0, font = ("Ubuntu Mono", 16, "bold"), show = "●")
    passbox.place(x=0,y=100+10)

    Frame(frame,width = 250, height = 1, bg = color_black).place(x=0,y=41+20)
    Frame(frame,width = 250, height = 1, bg = color_black).place(x=0,y=116+20)

    Label(frame, text = "Don't have an account yet?", font = ("Ubuntu Mono", 9), fg = color_black, bg = color_lightgray).place(x=0,y=138) 
    Button(frame, text = "Create one.", font = ("Ubuntu Mono", 9), fg = color_blue, bg = color_lightgray, borderwidth = 0, highlightthickness = 0, relief = "flat", command = open_signup).place(x=180,y=139)   
    
    # enter button
    Button(frame, image = enter, bg = color_lightgray, borderwidth = 0, highlightthickness = 0, relief = "flat", command = verify).place(x=200,y=175)

    login_window.mainloop()

if __name__ == "__main__":
    main()