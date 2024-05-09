"""ezpc_main.py"""
# This file contains the main program for EzPC: PC Parts Picker

import ezpc_functions
import gui_home, gui_login, gui_partselect, gui_signup
from ezpc_classes import *
import os.path, sqlite3

# Define database file to be used
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "ezpc.db")
DB = db_path

# DB = "ezpc.db"

""""""

def main():
    # Secure the connection to SQLite database
    connection = ezpc_functions.connect_db(DB)

    # Initiate user login and save to controller
    gui_login.main()

    # Open home window after successful login
    # gui_home.main(user)

    # If user is admin (root), access admin menu
    # if user.user_id == 1:
    #     ezpc_functions.admin_menu(connection)

if __name__ == "__main__":
    main()