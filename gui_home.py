import sqlite3
from tkinter import *
from PIL import Image, ImageTk
import pathlib, os

# controllers
def get_asset(img_file_name):
    curr_dir = pathlib.Path(__file__).parent.resolve()
    img_path = os.path.join(curr_dir, "assets", img_file_name)
    return img_path

def open_login():
    home_window.destroy()
    import gui_login
    gui_login.main()

#colors
color_black = "#323232"
color_lightgray = "#D9D9D9"
color_gray = "#9F9F9F"
color_lightblue = "#A5ABE2"
color_blue = "#6D79E2"
color_lightred = "#DE8E8E"
color_red = "#ED4D4D"

#window resolutions
reso_login = '300x400'
reso_home = '750x500'

#root window
home_window = Tk()
home_window.title('EZPC')
home_window.geometry(reso_home)
home_window.configure(bg = color_lightgray)
home_window.resizable(False,False)

#assets
img_icon = Image.open(get_asset("logo.png"))
res_icon = img_icon.resize((64,64), resample = 3)
icon = ImageTk.PhotoImage(res_icon)

img_save = Image.open(get_asset("save.png"))
res_save = img_save.resize((45,45), resample = 3)
save = ImageTk.PhotoImage(res_save)

header = Frame(home_window, width = 750, height = 82, bg = color_blue).place(x=0,y=0)
Label(header, image = icon, bg = color_blue).place(x=9,y=9)
Button(header, text = "logout", font = ("Ubuntu Mono", 14), fg = "white", bg = color_blue, borderwidth = 0, highlightthickness = 0, relief = "flat", command = open_login).place(x=650,y=28)
Button(header, text = "saved_builds", font = ("Ubuntu Mono", 14), fg = "white", bg = color_blue, borderwidth = 0, highlightthickness = 0, relief = "flat").place(x=520,y=28)


# part select frame
partselect_frame = Frame(home_window, width = 400, height = 393, bg = "red")
partselect_frame.place(x=25,y=107)

# summary frame
summary_frame = Frame(home_window, width = 275, height = 370, bg = color_gray)
summary_frame.place(x=450,y=107)

TOTAL_PRICE = "$XXXX.XX" # add total price here

Button(summary_frame, image = save, bg = color_gray, borderwidth = 0, highlightthickness = 0, relief = "flat").place(x=220,y=315)
Label(summary_frame, text = TOTAL_PRICE, fg = color_black, bg = color_gray, font = ("Ubuntu Mono", 24, "bold")).place(x=10,y=300)
Label(summary_frame, text = '*est. price', fg = color_black, bg = color_gray, font = ("Ubuntu Mono", 10)).place(x=20,y=335)

home_window.mainloop()