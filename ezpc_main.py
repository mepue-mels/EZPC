"""ezpc_main.py"""
# This file contains the main program for EzPC: PC Parts Picker

import ezpc_functions

# Define host name, user name, user password, and database to be used
HOST = "localhost"
NAME = "root"
PW = "walangpassword"
DB = "sql_ezpc"

""""""

def main():
    connection = ezpc_functions.create_db_connection(HOST, NAME, PW, DB)
    ezpc_functions.menu_login(connection)
    ezpc_functions.menu_main(connection)

if __name__ == "__main__":
    main()