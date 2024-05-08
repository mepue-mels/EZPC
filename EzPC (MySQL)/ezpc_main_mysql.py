"""ezpc_main.py"""
"""MySQL Implementation"""
# This file contains the main program for EzPC: PC Parts Picker

import ezpc_functions_mysql
from ezpc_classes_mysql import *

# Define host name, user name, user password, and database to be used
HOST = "localhost"
NAME = "root"
PW = "walangpassword"
DB = "sql_ezpc"

""""""

def main():
    # Secure the connection to SQL database
    connection = ezpc_functions_mysql.create_db_connection(HOST, NAME, PW, DB)

    # Initiate user login and save user attributes to a list
    user_attr = ezpc_functions_mysql.menu_login(connection)

    # Instantiate user object with user attributes from the user database
    user = User(user_attr[0],user_attr[1],user_attr[2])

    # Pass user object to access main menu
    ezpc_functions_mysql.menu_main(connection, user)

if __name__ == "__main__":
    main()