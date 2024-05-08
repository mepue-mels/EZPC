import sqlite3
from tkinter import *
from PIL import Image, ImageTk

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
img_icon = Image.open("c:/Users/K3lite/Documents/Repo/EZPC/assets/ezpc-01.png")
res_icon = img_icon.resize((64,64), resample = 3)
icon = ImageTk.PhotoImage(res_icon)

Frame(home_window, width = 750, height = 82, bg = color_blue).place(x=0,y=0)
Label(image = icon, bg = color_blue).place(x=9,y=9)


# part select frame
partselect_frame = Frame(home_window, width = 450, height = 393, bg = "red")
partselect_frame.place(x=25,y=107)

# summary frame
summary_frame = Frame(home_window, width = 225, height = 370, bg = "red")
summary_frame.place(x=500,y=107)

home_window.mainloop()