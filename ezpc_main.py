"""ezpc_main.py"""
# This file contains the main program for EzPC: PC Parts Picker

import ezpc_functions
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

    # Initiate user login from the database and save to controller
    user = ezpc_functions.menu_login(connection)

    # If user is admin (root), access admin menu
    if user.user_id == 1:
        ezpc_functions.admin_menu(connection)
        
    # Pass user object to access main menu
    ezpc_functions.menu_main(connection, user)

if __name__ == "__main__":
    main()