import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pathlib, os

# controllers
def get_asset(img_file_name):
    curr_dir = pathlib.Path(__file__).parent.resolve()
    img_path = os.path.join(curr_dir, "assets", img_file_name)
    return img_path

def open_home():
    partselect_window.destroy()
    import gui_home
    gui_home.main()

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
reso_home = '469x331'

#root window
partselect_window = Tk()
partselect_window.title('EZPC')
partselect_window.geometry(reso_home)
partselect_window.configure(bg = color_lightgray)
partselect_window.resizable(False,False)

#assets
img_back = Image.open(get_asset("back.png"))
res_back = img_back.resize((45,45), resample = 3)
back = ImageTk.PhotoImage(res_back)

header = Frame(partselect_window, width = 750, height = 82, bg = color_lightgray).place(x=0,y=0)
Button(header, image = back, bg = color_lightgray, borderwidth = 0, highlightthickness = 0, relief = "flat", command = open_home).place(x=18,y=18)
Label(header, text = "search", fg = color_black, bg = color_lightgray, font = ("Ubuntu Mono", 14)).place(x=410-275,y=25)
searchbox = Entry(header, width = 25, fg = color_black, bg = color_lightgray, border = 0, font = ("Ubuntu Mono", 14, "bold")).place(x=474-275,y=28)
Frame(header,width = 230, height = 1, bg = color_black).place(x=475-275,y=48)

# part select frame
partselect_frame = Frame(partselect_window, width = 700, height = 420, bg = "red")
partselect_frame.pack(fill=NONE, expand=TRUE)
partselect_frame.place(x=25,y=80)

# TESTING AREA
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "ezpc.db")
db = db_path
conn = sqlite3.connect(db)

def display():
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM cpu_data")

    tree = ttk.Treeview(partselect_frame)

    tree["columns"] = ("one", "two")
    tree.column("#0", width=0, stretch=NO)  # Hide main column
    tree.heading("#0", text="", anchor=W)  # Hide main column heading

    tree.column("one", width=300)
    tree.column("two", width=100)

    vsb = Scrollbar(partselect_frame, orient="vertical", command=tree.yview)
    vsb.pack(side=RIGHT, fill=BOTH)
    tree.configure(yscrollcommand=vsb.set)

    for row in cursor:
        tree.insert("", "end", values=row)

    tree.pack(fill=BOTH, expand=True)

display()

partselect_window.mainloop()