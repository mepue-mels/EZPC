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
login_window = Tk()
login_window.title(' ')
login_window.geometry(reso_login)
login_window.configure(bg = color_lightgray)
login_window.resizable(False,False)

#assets
img_icon = Image.open("c:/Users/K3lite/Documents/Repo/EZPC/assets/ezpc-01.png")
res_icon = img_icon.resize((64,64), resample = 3)
icon = ImageTk.PhotoImage(res_icon)

img_enter = Image.open("c:/Users/K3lite/Documents/Repo/EZPC/assets/login_enter.png")
res_enter = img_enter.resize((45,45), resample = 3)
enter = ImageTk.PhotoImage(res_enter)

Frame(login_window, width = 300, height = 120, bg = color_blue).place(x=0,y=0)

Label(image = icon, bg = color_blue).place(x=118,y=28)

frame = Frame(login_window, width = 250, height = 225, bg = color_lightgray)
frame.place(x=25,y=150)

usertext = Label(frame, text = 'username', fg = color_black, bg = color_lightgray, font = ("Ubuntu Mono", 14))
usertext.place(x=0,y=0+10)
passtext = Label(frame, text = 'password', fg = color_black, bg = color_lightgray, font = ("Ubuntu Mono", 14))
passtext.place(x=0,y=75+10)

userbox = Entry(frame, width = 25, fg = color_black, bg = color_lightgray, border = 0, font = ("Ubuntu Mono", 16, "bold"))
userbox.place(x=0,y=25+10)
passbox = Entry(frame, width = 25, fg = color_black, bg = color_lightgray, border = 0, font = ("Ubuntu Mono", 16, "bold"), show = "*")
passbox.place(x=0,y=100+10)

Frame(frame,width = 250, height = 1, bg = color_black).place(x=0,y=41+20)
Frame(frame,width = 250, height = 1, bg = color_black).place(x=0,y=116+20)

Button(frame, image = enter, bg = color_lightgray, borderwidth = 0, highlightthickness = 0, relief = "flat").place(x=200,y=160)     

login_window.mainloop()