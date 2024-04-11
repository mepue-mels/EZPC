"""ezpc_main.py"""
# This file contains the main program for EzPC: PC Parts Picker

import ezpc_functions

""""""

def main():
    connection = ezpc_functions.create_db_connection("localhost", "root", "walangpassword", "sql_ezpc")
    ezpc_functions.menu_login(connection)
    ezpc_functions.menu_main(connection)

if __name__ == "__main__":
    main()