"""ezpc_functions.py"""
# This file contains the functions used for EzPC: PC Parts Picker

from ezpc_queries import *
from ezpc_classes import *
import os.path, sqlite3

# Define database file to be used
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "ezpc.db")
DB = db_path

""" SERVER FUNCTIONS """

# Function to initialize connection to database file
def connect_db(db):
    print("Connecting to database . . . .")
    try:
        # Connect to the database
        conn = sqlite3.connect(db)
        print("Database connection successful.")
        return conn
    
    except sqlite3.Error as e:
        print(f"Error connecting to database: '{e}'")
        exit()

# Function to execute SQLite queries
def execute_query(db, query, fetchall=True):
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute(query)

        if fetchall:
            results = cursor.fetchall()
        else:
            results = cursor.fetchone()

        conn.commit()
        return results

    except sqlite3.Error as e:
        print("Error executing query:", e)
        exit()

""" LOGIN FUNCTIONS """

# Function to add username and password to database
# User can enter 0 to exit the program
def create_user(un = " ", pw = " "):
    connection = sqlite3.connect(DB)
    while True:
        print("---USER REGISTER---")
        print("Enter 0 to exit the program.")

        # # Username and password must be 3 or more characters in length
        # username = input("Enter username (3 or more characters): ")
        # if username == "0":
        #     exit()
        # password = input("Enter password (3 or more characters): ")
        # if password == "0":
        #     exit()

        # Check if username or password passes length requirement
        # if len(un) < 3 or len(pw) < 3:
        #     print("Username or password too short.")
        #     continue

        # Execute a SELECT query if the username already exists in the database
        cursor = connection.cursor()
        cursor.execute(user_select_username_query, (un,))

        # Check if any results were returned
        if cursor.fetchone(): # The user inputted an existing username
            print("The username already exists in the database. Try again.")
            return True
        else: # The user inputted a unique username
            cursor.execute("SELECT * FROM user_details WHERE user_id = (SELECT MAX(user_id) FROM user_details);")
            uid = cursor.fetchone()[0] + 1
            cursor.execute(user_insert_query, (uid, un, pw))
            connection.commit()
            print("User added to the database.")
            return False
    
# Function to check if username and password is in database
# User can enter 0 to exit the program
# Returns user record as list
def login_user(un = " ", pw = " "):
    connection = sqlite3.connect(DB)
    print("---USER LOGIN---")
    print("Enter 0 to exit the program.")
    print(un + " " + pw)
    while True:
        # username = input("Enter username: ")
        # if username == "0":
        #     exit()
        # password = input("Enter password: ")
        # if password == "0":
        #     exit()

        # Execute a SELECT query to check if the username and password combination exists
        cursor = connection.cursor()
        cursor.execute(verify_login_query, (un, pw))

        # Check if any rows were returned
        result = cursor.fetchone()
        if result:
            print("Login successful.")
            user = User(result[0],result[1],result[2])
            return user
        else:
            print("Username and password combination does not exist in the database.")
            return


""" DATA DISPLAY FUNCTIONS """

# Function to display the user's current build and the total price
def display_current_build(user = User, pc = Computer):
    if pc.comp_name is not None:
        print(f"---\"{pc.comp_name}\"---")
    else:
        print(f"---{user.user_name.upper()}'S CURRENT PC BUILD---")
    print(f"""[2] Case: {pc.part_list[0][1]}
[3] Cooler: {pc.part_list[1][1]}
[4] CPU: {pc.part_list[2][1]}
[5] GPU: {pc.part_list[3][1]}
[6] Motherboard: {pc.part_list[4][1]}
[7] Power Supply: {pc.part_list[5][1]}
[8] RAM: {pc.part_list[6][1]}
[9] Storage: {pc.part_list[7][1]}""")
    
    price = 0
    for i in range(0,8):
        price += pc.part_list[i][2]
    print(f"Price: {price}",end="")
    return price

# Function to display the user's saved PC builds from the database
def display_saved_build(user = User):
    print(f"---{user.user_name.upper()}'S SAVED BUILDS---")
    for x in range(0,len(user.pc_list)-1):
        print(f"[{user.pc_list[x].comp_id}] {user.pc_list[x].comp_name}")

""" DATA CRUD FUNCTIONS """

# Function to retrieve PC builds owned by the user from the database
def read_pc_list(user = User):
    connection = sqlite3.connect(DB)
    # Check for existing PC builds by the user
    cursor = connection.cursor()
    cursor.execute(pc_select_query, (user.user_id,))

    result = cursor.fetchall()
    # cursor.close()
    if result:
        for row in result:
            # Initialize new Computer class
            comp = Computer(user.user_id,row[0],row[1])

            # Populate using part IDs
            cursor = connection.cursor()

            # cursor.execute(part_select_case_query, (row[2],))
            # comp.part_list[0] = cursor.fetchone()
            # cursor.execute(part_select_cooler_query, (row[3],))
            # comp.part_list[1] = cursor.fetchone()
            # cursor.execute(part_select_cpu_query, (row[4],))
            # comp.part_list[2] = cursor.fetchone()
            # cursor.execute(part_select_gpu_query, (row[5],))
            # comp.part_list[3] = cursor.fetchone()
            # cursor.execute(part_select_mobo_query, (row[6],))
            # comp.part_list[4] = cursor.fetchone()
            # cursor.execute(part_select_psu_query, (row[7],))
            # comp.part_list[5] = cursor.fetchone()
            # cursor.execute(part_select_ram_query, (row[8],))
            # comp.part_list[6] = cursor.fetchone()
            # cursor.execute(part_select_storage_query, (row[9],))
            # comp.part_list[7] = cursor.fetchone()

            for i in range(8):
                if row[i+2] == None:
                    comp.part_list[i] = [None,None,0,None,None,None,None,None,None,None]
                    continue
                
                cursor.execute(part_select_query_list[i], (int(row[i+2]),))
                comp.part_list[i] = cursor.fetchone()

            # Append to user PC list
            user.add_pc(comp)

        # print(repr(comp))
        cursor.close()
        print(user.pc_list)
    return
      
# Function to update case in current PC build
def update_case(connection, pc = Computer):
    print("---CASE SELECTOR---")
    while True:
        try:
            id = int(input("Type in desired case ID for your PC: "))
        except ValueError:
            print("Invalid ID.")
            continue

        # Execute a SELECT query and check if the case ID exists in the database
        cursor = connection.cursor()
        cursor.execute(part_select_case_query, (id,))

        result = cursor.fetchone()
        if result:
            pc.part_list[0] = result
            print("Case added to PC!")
            return 1
        else:
            print(f"Case ID {id} does not exist in database.")

# Function to update cooler in current PC build
def update_cooler(connection, pc = Computer):
    print("---COOLER SELECTOR---")
    while True:
        try:
            id = int(input("Type in desired cooler ID for your PC: "))
        except ValueError:
            print("Invalid ID.")
            continue

        # Execute a SELECT query and check if the cooler ID exists in the database
        cursor = connection.cursor()
        cursor.execute(part_select_cooler_query, (id,))

        result = cursor.fetchone()
        if result:
            pc.part_list[1] = result
            print("Cooler added to PC!")
            return 1
        else:
            print(f"Cooler ID {id} does not exist in database.")

# Function to update CPU in current PC build
def update_cpu(connection, pc = Computer):
    print("---CPU SELECTOR---")
    while True:
        try:
            id = int(input("Type in desired CPU ID for your PC: "))
        except ValueError:
            print("Invalid ID.")
            continue

        # Execute a SELECT query and check if the CPU ID exists in the database
        cursor = connection.cursor()
        cursor.execute(part_select_cpu_query, (id,))

        result = cursor.fetchone()
        if result:
            pc.part_list[2] = result
            print("CPU added to PC!")
            return 1
        else:
            print(f"CPU ID {id} does not exist in database.")

# Function to update GPU in current PC build
def update_gpu(connection, pc = Computer):
    print("---GPU SELECTOR---")
    while True:
        try:
            id = int(input("Type in desired GPU ID for your PC: "))
        except ValueError:
            print("Invalid ID.")
            continue

        # Execute a SELECT query and check if the GPU ID exists in the database
        cursor = connection.cursor()
        cursor.execute(part_select_gpu_query, (id,))

        result = cursor.fetchone()
        if result:
            pc.part_list[3] = result
            print("GPU added to PC!")
            return 1
        else:
            print(f"GPU ID {id} does not exist in database.")

# Function to update motherboard in current PC build
def update_mobo(connection, pc = Computer):
    print("---MOTEHRBOARD SELECTOR---")
    while True:
        try:
            id = int(input("Type in desired motherboard ID for your PC: "))
        except ValueError:
            print("Invalid ID.")
            continue

        # Execute a SELECT query and check if the motherboard ID exists in the database
        cursor = connection.cursor()
        cursor.execute(part_select_mobo_query, (id,))

        result = cursor.fetchone()
        if result:
            pc.part_list[4] = result
            print("Motherboard added to PC!")
            return 1
        else:
            print(f"Motherboard ID {id} does not exist in database.")

# Function to update power supply in current PC build
def update_psu(connection, pc = Computer):
    print("---POWER SUPPLY SELECTOR---")
    while True:
        try:
            id = int(input("Type in desired power supply ID for your PC: "))
        except ValueError:
            print("Invalid ID.")
            continue

        # Execute a SELECT query and check if the power supply ID exists in the database
        cursor = connection.cursor()
        cursor.execute(part_select_psu_query, (id,))

        result = cursor.fetchone()
        if result:
            pc.part_list[5] = result
            print("Power supply added to PC!")
            return 1
        else:
            print(f"Power supply ID {id} does not exist in database.")

# Function to update RAM in current PC build
def update_ram(connection, pc = Computer):
    print("---RAM SELECTOR---")
    while True:
        try:
            id = int(input("Type in desired RAM ID for your PC: "))
        except ValueError:
            print("Invalid ID.")
            continue

        # Execute a SELECT query and check if the RAM ID exists in the database
        cursor = connection.cursor()
        cursor.execute(part_select_ram_query, (id,))

        result = cursor.fetchone()
        if result:
            pc.part_list[6] = result
            print("RAM added to PC!")
            return 1
        else:
            print(f"RAM ID {id} does not exist in database.")

# Function to update storage in current PC build
def update_storage(connection, pc = Computer):
    print("---STORAGE SELECTOR---")
    while True:
        try:
            id = int(input("Type in desired storage ID for your PC: "))
        except ValueError:
            print("Invalid ID.")
            continue

        # Execute a SELECT query and check if the storage ID exists in the database
        cursor = connection.cursor()
        cursor.execute(part_select_storage_query, (id,))

        result = cursor.fetchone()
        if result:
            pc.part_list[7] = result
            print("Storage added to PC!")
            return 1
        else:
            print(f"Storage ID {id} does not exist in database.")

# Function to save the current PC build
# Called when the user attempts to exit the program
def update_pc(connection, user = User, pc = Computer, change = bool):
    if change == 0:
        return
    print("Do you want to save this PC build? ",end="")
    choice = input("(Y/N): ")
    if choice == "Y" or choice == "y":
        # If PC already exists and is updated
        if pc != user.pc_list[-1]:
            cursor = connection.cursor()
            cursor.execute(pc_update_query, (pc.part_list[0][0],
                                            pc.part_list[1][0],
                                            pc.part_list[2][0],
                                            pc.part_list[3][0],
                                            pc.part_list[4][0],
                                            pc.part_list[5][0],
                                            pc.part_list[6][0],
                                            pc.part_list[7][0],
                                            pc.comp_id))
            connection.commit()
        
        # If PC is new and will be saved
        else:
            # Takes new PC name
            name = input("Enter PC name: ").strip()
            i = 1
            new_name = name
            # Check if database already has PC with same name
            while any(getattr(pc, "comp_name", None) == new_name for pc in user.pc_list):
                if pc.user_id == user.user_id:
                    i += 1
                    new_name = f"{name} ({i})"

            # newest PC accessed from the last because it is appended to pc_list
            cursor = connection.cursor()
            cursor.execute(pc_insert_query, (user.user_id,new_name,
                                            pc.part_list[0][0],
                                            pc.part_list[1][0],
                                            pc.part_list[2][0],
                                            pc.part_list[3][0],
                                            pc.part_list[4][0],
                                            pc.part_list[5][0],
                                            pc.part_list[6][0],
                                            pc.part_list[7][0]))
            connection.commit()
        print("PC saved successfully.")

def delete_pc(connection, pc = Computer):
    print("Are you sure you want to delete this PC from the database? ", end="")
    choice = input("(Y/N): ")
    if choice == "Y" or choice == "y":
        cursor = connection.cursor()
        cursor.execute(pc_delete_query, (pc.comp_id,))
        connection.commit()
        print("PC deleted successfully.")
        cursor.close()
        return 1
    elif choice == "N" or choice == "n":
        print("Delete operation aborted.")
        return 0
    else:
        print("Invalid option.")
        return 0

""" USER NAV FUNCTIONS """

# Function to display the menu for user login
# User can enter 0 to exit the program
def menu_login(connection):
    menu = -1
    while menu != 0:
        menu = int(input("---LOGIN MENU---\n[0] EXIT\n[1] LOGIN\n[2] REGISTER\nSelect option: "))
        if menu == 0:
            exit()
        elif menu == 1:
            return login_user(connection)
        elif menu == 2:
            create_user(connection)
        else:
            print("Out of range.")

# Function to display the main menu for the EzPC program
# Entering 0 will prompt the user if they wish to save the
# PC build into the SQL database
def menu_main(user = User):
    connection = sqlite3.connect(DB)
    # Retrieve saved PC builds from database, if any
    read_pc_list(user)

    # Initialize new PC build by default and append to PC list
    pc = user.new_pc()

    # print(user.pc_list[1].part_list)
    print(f"Welcome back, {user.user_name}!")
    price = display_current_build(user, pc)
    return price
    # menu = -1
    # change = 0
    # while menu != 0:
    #     display_current_build(user, pc)
    #     try:
    #         menu = int(input(display_main_menu))
    #     except:
    #         print("Invalid option.")
    #         continue
    #     if menu == -1:
    #         flag = delete_pc(connection, pc)
    #         if flag:
    #             user.init_pc_list()
    #             read_pc_list(connection, user)
    #             pc = user.new_pc()
    #             change = 0
    #     elif menu == 0:
    #         if change == 1:
    #             update_pc(connection, user, pc, change)
    #         exit()
    #     elif menu == 1: # explore saved builds
    #         pc = menu_build(user)
    #         # Reset save flag to unchanged (0) if user switches to new PC build
    #         if pc != user.pc_list[-1]:
    #             change = 0
    #     elif menu == 2: # case
    #         change = update_case(connection, pc)
    #     elif menu == 3: # cooler
    #         change = update_cooler(connection, pc)
    #     elif menu == 4: # cpu
    #         change = update_cpu(connection, pc)
    #     elif menu == 5: # gpu
    #         change = update_gpu(connection, pc)
    #     elif menu == 6: # mobo
    #         change = update_mobo(connection, pc)
    #     elif menu == 7: # psu
    #         change = update_psu(connection, pc)
    #     elif menu == 8: # ram
    #         change = update_ram(connection, pc)
    #     elif menu == 9: # storage
    #         change = update_storage(connection, pc)

# Function to display the PC build selection menu
# Called when the user presses [1]
def menu_build(user = User):
    display_saved_build(user)
    print("---SAVED BUILDS MENU---\n[-1] BACK\n[0] NEW PC")
    while True:
        try:
            choice = int(input("Select PC ID to load: "))
        except:
            print("Invalid PC ID.")
            continue
        if choice == -1:
            return user.pc_list[-1]
        elif choice == 0:
            user.pop_pc()
            return user.new_pc()
        for x in user.pc_list:
            if x.comp_id == choice:
                return x
        print("Invalid PC ID.")
    

""" ADMIN FUNCTIONS"""

# Function to display the admin menu for the EzPC program
# Admin can enter 0 to exit the program
# The admin menu can only be accessed by the "root" user
# The admin menu can be used to check and delete users from the database
def admin_menu(connection):
    menu = -1
    while menu != 0:
        menu = int(input("---ADMIN MENU---\n[-1] BACK\n[0] EXIT\n[1] USERS\n[2] PARTS\nSelect option: "))
        if menu == -1:
            return
        elif menu == 0:
            exit()
        elif menu == 1:
            admin_menu_user(connection)
        elif menu == 2:
            admin_menu_part(connection)

# Function to display the user editing menu for the EzPC program
# Admin can enter 0 to exit the program
# Admin can enter -1 to return to the admin menu
def admin_menu_user(connection):
    menu = -1
    while menu != 0:
        menu = int(input("---USER EDITING MENU---\n[-1] BACK\n[0] EXIT\n[1] CHECK\n[2] DELETE\nSelect option: "))
        if menu == -1:
            return
        elif menu == 0:
            exit()
        elif menu == 1:
            admin_check_user(connection)
        elif menu == 2:
            admin_delete_user(connection)

# Function to display the parts editing menu for the EzPC program
# Admin can enter 0 to exit the program
# Admin can enter -1 to return to the admin menu
def admin_menu_part(connection):
        menu = -1
        while menu != 0:
            menu = int(input("---PARTS EDITING MENU---\n[-1] BACK\n[0] EXIT\n[1] CHECK\n[2] DELETE\nSelect option: "))
            if menu == -1:
                return
            elif menu == 0:
                exit()
            elif menu == 1:
                admin_check_part(connection)
            elif menu == 2:
                admin_delete_part(connection)

# Function to check if the user exists in the database
# Admin can enter 0 to exit the program
# Admin can enter -1 to return to the admin menu
def admin_check_user(connection):
    print("---CHECK USER---\n[-1] BACK\n[0] EXIT")
    while True:
        username = input("Enter username to check in the database: ")
        if username == "0":
            exit()
        if username == "-1":
            return
        cursor = connection.cursor()
        cursor.execute(user_select_username_query, (username,))

        # Check if any results were returned
        result = cursor.fetchone()
        if result:
            print("User exists in the database.")
            str1 = "User ID"
            str2 = "Username"
            str3 = "Password"
            r1 = str(result[0])
            r2 = str(result[1])
            r3 = str(result[2])
            print(str1.center(10), str2.center(15), str3.center(15))
            print(r1.center(10), r2.center(15), r3.center(15))
        else:
            print("User does not exist in the database.")

# Function to delete the user in the database
# Admin can enter 0 to exit the program
# Admin can enter -1 to return to the admin menu
def admin_delete_user(connection):
    print("---DELETE USER---\n[-1] BACK\n[0] EXIT")
    while True:
        username = input("Enter username to delete in the database: ")
        if username == "0":
            exit()
        if username == "-1":
            return
        
        # Check if user exists in the database
        cursor = connection.cursor()
        cursor.execute(user_select_username_query, (username,))
        result = cursor.fetchone()
        cursor.close()
        if not result:
            print("User does not exist in the database.")
        else:
            str1 = "User ID"
            str2 = "Username"
            str3 = "Password"
            r1 = str(result[0])
            r2 = str(result[1])
            r3 = str(result[2])
            print(str1.center(10), str2.center(15), str3.center(15))
            print(r1.center(10), r2.center(15), r3.center(15))

            print("Are you sure you want to delete this user from the database? ", end="")
            choice = input("(Y/N): ")
            if choice == "Y" or choice == "y":
                cursor = connection.cursor()
                cursor.execute(user_delete_query, (username,))
                connection.commit()
                print("User", username, "deleted successfully.")
                cursor.close()
            elif choice == "N" or choice == "n":
                print("Delete operation aborted.")
            else:
                print("Invalid option.")
                return

def admin_check_part(connection):
    pass

def admin_delete_part(connection):
    pass

""" EXIT FUNCTION """

# Function to exit the program
def exit():
    print("Exiting program.")
    raise SystemExit