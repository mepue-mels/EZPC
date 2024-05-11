"""gui_home.py"""

import sqlite3
from tkinter import *
from PIL import Image, ImageTk
import pathlib, os
from ezpc_functions import *

def main(user, pc):
    # controllers
    def get_asset(img_file_name):
        curr_dir = pathlib.Path(__file__).parent.resolve()
        img_path = os.path.join(curr_dir, "assets", img_file_name)
        return img_path

    def open_login():
        home_window.destroy()
        import gui_login
        gui_login.main()

    def open_partselect(part):
        # print("\n" + part)
        home_window.destroy()
        import gui_partselect
        gui_partselect.main(user, part)
        # return

    # colors
    color_black = "#323232"
    color_gray = "#9F9F9F"
    color_lightgray = "#D9D9D9"
    color_lightergray = "#E8E8E8"
    color_lightblue = "#A5ABE2"
    color_blue = "#6D79E2"
    color_lightred = "#DE8E8E"
    color_red = "#ED4D4D"

    # window resolutions
    reso_login = '300x400'
    reso_home = '750x500'

    # root window
    home_window = Tk()
    home_window.title('EZPC')
    home_window.geometry(reso_home)
    home_window.configure(bg = color_lightgray)
    home_window.resizable(False,False)

    # assets
    img_icon = Image.open(get_asset("logo.png"))
    res_icon = img_icon.resize((64,64), resample = 3)
    icon = ImageTk.PhotoImage(res_icon)

    img_save = Image.open(get_asset("save.png"))
    res_save = img_save.resize((45,45), resample = 3)
    save = ImageTk.PhotoImage(res_save)

    img_case = Image.open(get_asset("part_case.png"))
    res_case = img_case.resize((64,64), resample=3)
    part_case = ImageTk.PhotoImage(res_case)

    # header frame
    header = Frame(home_window, width = 750, height = 82, bg = color_blue).place(x=0,y=0)
    Label(header, image = icon, bg = color_blue).place(x=9,y=9)
    Button(header, text = "logout", font = ("Ubuntu Mono", 14), fg = "white", bg = color_blue, borderwidth = 0, highlightthickness = 0, relief = "flat", command = open_login).place(x=650,y=28)
    # Button(header, text = "saved builds", font = ("Ubuntu Mono", 14), fg = "white", bg = color_blue, borderwidth = 0, highlightthickness = 0, relief = "flat").place(x=520,y=28)

    # part select frame
    partselect_frame = Frame(home_window, width = 400, height = 370, bg = color_gray)
    partselect_frame.place(x=25,y=107)

    # spacer for inner padding
    spacer_label = Label(partselect_frame, text="", bg=color_gray)
    spacer_label.grid(row=0,column=0,padx=2,pady=2)
    
    case_button = Button(spacer_label, text="case", width=25-2, height=5, fg=color_black, bg=color_lightgray, font = ("Ubuntu Mono", 10), borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground=color_lightergray, command=lambda: open_partselect(case_button.cget("text")))
    case_button.grid(row=0, column=0, padx=2, pady=2)
    
    cooler_button = Button(spacer_label, text="cooler", width=25-2, height=5, fg=color_black, bg=color_lightgray, font = ("Ubuntu Mono", 10), borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground=color_lightergray, command=lambda: open_partselect(cooler_button.cget("text")))
    cooler_button.grid(row=0, column=1, padx=2, pady=2)

    cpu_button = Button(spacer_label, text="cpu", width=25-2, height=5, fg=color_black, bg=color_lightgray, font = ("Ubuntu Mono", 10), borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground=color_lightergray, command=lambda: open_partselect(cpu_button.cget("text")))
    cpu_button.grid(row=1, column=0, padx=2, pady=2)

    gpu_button = Button(spacer_label, text="gpu", width=25-2, height=5, fg=color_black, bg=color_lightgray, font = ("Ubuntu Mono", 10), borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground=color_lightergray, command=lambda: open_partselect(gpu_button.cget("text")))
    gpu_button.grid(row=1, column=1, padx=2, pady=2)

    mobo_button = Button(spacer_label, text="mobo", width=25-2, height=5, fg=color_black, bg=color_lightgray, font = ("Ubuntu Mono", 10), borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground=color_lightergray, command=lambda: open_partselect(mobo_button.cget("text")))
    mobo_button.grid(row=2, column=0, padx=2, pady=2)

    psu_button = Button(spacer_label, text="psu", width=25-2, height=5, fg=color_black, bg=color_lightgray, font = ("Ubuntu Mono", 10), borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground=color_lightergray, command=lambda: open_partselect(psu_button.cget("text")))
    psu_button.grid(row=2, column=1, padx=2, pady=2)

    ram_button = Button(spacer_label, text="ram", width=25-2, height=5, fg=color_black, bg=color_lightgray, font = ("Ubuntu Mono", 10), borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground=color_lightergray, command=lambda: open_partselect(ram_button.cget("text")))
    ram_button.grid(row=3, column=0, padx=2, pady=2)

    storage_button = Button(spacer_label, text="storage", width=25-2, height=5, fg=color_black, bg=color_lightgray, font = ("Ubuntu Mono", 10), borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground=color_lightergray, command=lambda: open_partselect(storage_button.cget("text")))
    storage_button.grid(row=3, column=1, padx=2, pady=2)

    # summary frame
    summary_frame = Frame(home_window, width = 275, height = 370-2, bg = color_gray)
    summary_frame.place(x=450,y=107)
    summary_frame.grid_propagate(False)
    
    # part list
    part_list = pc.get_part_list()
    print(part_list)
    name_list = []
    price_list = []
    labels = []

    for x in range(8):
        if part_list[x][1]:
            name_list.append(part_list[x][1])
            price_list.append(part_list[x][2])

    print(name_list)
    print(price_list)

    for i in range(0,17):
        part_label = Label(summary_frame, text="", padx=1, pady=0, fg = color_black, bg = color_gray)
        part_label.grid(row=i,column=0,sticky='w')
        if i % 2 != 0:
            part_label.config(font = ("Ubuntu Mono", 9))
        else:
            part_label.config(font = ("Ubuntu Mono", 7))
        labels.append(part_label)

    for i in range(len(name_list)):
        labels[(i+1)*2-1].config(text="  " + name_list[i])
        labels[(i+1)*2].config(text=f"      ₱{price_list[i]:.2f}")

    price = 0
    for i in range(0,8):
        price += part_list[i][2]
    TOTAL_PRICE = f"₱{price:.2f}" # add total price here

    summary_frame.config(width = 275, height = 370-2)

    # Button(summary_frame, image = save, bg = color_gray, borderwidth = 0, highlightthickness = 0, relief = "flat", activebackground=color_gray).place(x=220,y=315)
    Label(summary_frame, text = TOTAL_PRICE, fg = color_black, bg = color_gray, font = ("Ubuntu Mono", 24, "bold")).place(x=10,y=300)
    Label(summary_frame, text = '*est. price', fg = color_black, bg = color_gray, font = ("Ubuntu Mono", 10)).place(x=20,y=335)

    home_window.mainloop()

if __name__ == "__main__":
    main(user = User, pc = Computer)