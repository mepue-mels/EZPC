import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pathlib, os
from ezpc_functions import *

def main(user, part):
    # controllers
    def get_asset(img_file_name):
        curr_dir = pathlib.Path(__file__).parent.resolve()
        img_path = os.path.join(curr_dir, "assets", img_file_name)
        return img_path

    def open_home(part):
        partselect_window.destroy()
        import gui_home
        gui_home.main(user, user.pc_list[-1])

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
    reso_home = '469x360'

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
    
    match part:
        case "mobo":
            selected_table = "mobo_data"
            selected_part = "motherboard"
        case "cpu":
            selected_table = "cpu_data"
            selected_part = "processor"
        case "cooler":
            selected_table = "cooler_data"
            selected_part = "cooler"
        case "ram":
            selected_table = "ram_data"
            selected_part = "memory"
        case "gpu":
            selected_table = "gpu_data"
            selected_part = "graphics"
        case "storage":
            selected_table = "storage_data"
            selected_part = "storage"
        case "psu":
            selected_table = "psu_data"
            selected_part = "power"
        case "case":
            selected_table = "case_data"
            selected_part = "case"
        case _:
            print("Error")
            raise SystemExit
    
    partselect_header = Frame(partselect_window, width = 450, height = 82, bg = color_lightgray).place(x=0,y=0)
    Button(partselect_header, image = back, bg = color_lightgray, borderwidth = 0, highlightthickness = 0, relief = "flat").place(x=18,y=18)
    Label(partselect_header, text=selected_part, fg=color_black, bg=color_lightgray, font=("Ubuntu Mono", 40, "bold")).place(x=80,y=18)

    # part select frame
    partselect_frame = Frame(partselect_window, width = 700, height = 420, bg = color_blue)
    partselect_frame.pack(fill=NONE, expand=TRUE)
    partselect_frame.place(x=25,y=80)
    
    # part adding
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "ezpc.db")
    db = db_path
    conn = sqlite3.connect(db)

    def display():
        
        cursor = conn.cursor()
        cursor.execute("SELECT name, price, id FROM " + selected_table)

        tree = ttk.Treeview(partselect_frame)

        tree["columns"] = ("one", "two", "three")
        tree.column("#0", width=0, stretch=NO)  # Hide main column
        tree.heading("#0", text="", anchor=W)  # Hide main column heading

        tree.column("one", width=300)
        tree.column("two", width=100)
        tree.column("three", width=0, minwidth=0) # hide ID

        tree.heading("one", text="Part", anchor=W)
        tree.heading("two", text="Price", anchor=W)

        vsb = Scrollbar(partselect_frame, orient="vertical", command=tree.yview)
        vsb.pack(side=RIGHT, fill=BOTH)
        tree.configure(yscrollcommand=vsb.set)

        for row in cursor:
            tree.insert("", "end", values=row)

        tree.pack(fill=BOTH, expand=True)

        # Initialize search_var properly
        search_var = StringVar()
        
        # Search filter
        search_entry = Entry(partselect_frame, textvariable=search_var)
        search_entry.pack(pady=5)
        
        def update_treeview(*args):
            search_term = search_var.get().lower()

            # Clear existing items in the treeview
            for item in tree.get_children():
                tree.delete(item)

            # Fetch data from the database again based on the search term
            cursor.execute("SELECT name, price, id FROM " + selected_table)
            for row in cursor:
                if any(search_term in str(cell).lower() for cell in row):
                    tree.insert("", "end", values=row)

        # Bind update_treeview to changes in the search_var
        search_var.trace_add('write', update_treeview)

        def add_to_list():
            selected_item = tree.focus()
            item_values = tree.item(selected_item, 'values')
            if item_values:
                match part:
                    case "mobo":
                        update_mobo(user.pc_list[-1], item_values[2])
                    case "cpu":
                        update_cpu(user.pc_list[-1], item_values[2])
                    case "cooler":
                        update_cooler(user.pc_list[-1], item_values[2])
                    case "ram":
                        update_ram(user.pc_list[-1], item_values[2])
                    case "gpu":
                        update_gpu(user.pc_list[-1], item_values[2])
                    case "storage":
                        update_storage(user.pc_list[-1], item_values[2])
                    case "psu":
                        update_psu(user.pc_list[-1], item_values[2])
                    case "case":
                        update_case(user.pc_list[-1], item_values[2])


                print("Selected Item:", item_values)
                messagebox.showinfo(title="Nice!", message="Part added!")
                open_home(part)

        tree.bind("<Double-1>", lambda event: add_to_list())

    display()

    partselect_window.mainloop()


if __name__ == "__main__":
    main(user = User, part = str)