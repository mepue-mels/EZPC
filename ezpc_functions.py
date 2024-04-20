"""ezpc_functions.py"""
# This file contains the functions used for EzPC: PC Parts Picker

import mysql.connector
from mysql.connector import Error
import pandas as pd
from ezpc_queries import *

""""""

# Function to initialize MySQL server connection
def create_server_connection(host_name, user_name, user_password):
    pass
    connection = None
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Function to initialize database connection
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Function to execute SQL queries
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

""""""

# Function to display the menu for login
# User can enter 0 to exit the program
def menu_login(connection):
    menu = -1
    while menu != 0:
        menu = int(input("---MENU---\n[0] EXIT\n[1] LOGIN\n[2] REGISTER\nSelect option: "))
        if menu == 0:
            exit()
        elif menu == 1:
            user_login(connection)
            return
        elif menu == 2:
            user_insert(connection)
        else:
            print("Out of range.")

# Function to add username and password to database
# User can enter 0 to exit the program
def user_insert(connection):
    count = 0
    while True:
        count += 1
        print("---REGISTER---")
        print("Enter 0 to exit the program.")

        # Username and password must be 3 or more characters in length
        username = input("Enter username (3 or more characters): ")
        if username == "0":
            exit()
        password = input("Enter password (3 or more characters): ")
        if password == "0":
            exit()

        # Check if username or password passes length requirement
        if len(username) < 3 or len(username) < 3:
            print("Username or password too short.")
            continue

        # Execute a SELECT query if the username already exists in the database
        cursor = connection.cursor()
        cursor.execute(check_username_query, (username,))

        # Check if any results were returned
        if count >= 3:
            print("Too many tries.")
            exit()
        if cursor.fetchone(): # The user inputted an existing username
            print("The username already exists in the database. Try again.")
        else: # The user inputted a unique username
            cursor.execute("SELECT LAST_INSERT_ID()")
            uid = cursor.fetchone()[0]
            cursor.execute(user_insert_query, (uid, username, password))
            connection.commit()
            print("User added to the database.")
            break
    
# Function to check if username and password is in database
# User can enter 0 to exit the program
def user_login(connection):
    print("---LOGIN---")
    print("Enter 0 to exit the program.")
    username = input("Enter username: ")
    if username == "0":
        exit()
    password = input("Enter password: ")
    if password == "0":
        exit()

    # Execute a SELECT query to check if the username and password combination exists
    cursor = connection.cursor()
    cursor.execute(verify_login_query, (username, password))

    # Check if any rows were returned
    result = cursor.fetchone()
    if result[1] == "root":
        print("Admin access granted.")
        # cursor.close()
        menu_admin(connection)
        return
    elif result:
        print("Username and password combination exists in the database.")
        return
    else:
        print("Username and password combination does not exist in the database.")
        exit()

""""""

# Function to display the main menu for the EzPC program
def menu_main(connection):
    menu = -1
    while menu != 0:
        menu = int(input("---EZPC MENU---\n[0] EXIT\n[1]\nSelect option: "))
        if menu == 0:
            exit()

""""""

# Function to display the admin menu for the EzPC program
# Admin can enter 0 to exit the program
# The admin menu can only be accessed by the "root" user
# The admin menu can be used to check and delete users from the database
def menu_admin(connection):
    menu = -1
    while menu != 0:
        menu = int(input("---ADMIN MENU---\n[0] EXIT\n[1] USERS\n[2] PARTS\nSelect option: "))
        if menu == 0:
            exit()
        elif menu == 1:
            menu_admin_user(connection)
        elif menu == 2:
            menu_admin_parts(connection)

# Function to display the user editing menu for the EzPC program
# Admin can enter 0 to exit the program
# Admin can enter -1 to return to the admin menu
def menu_admin_user(connection):
    menu = -1
    while menu != 0:
        menu = int(input("---USER EDITING MENU---\n[-1] BACK\n[0] EXIT\n[1] CHECK\n[2] DELETE\nSelect option: "))
        if menu == -1:
            return
        elif menu == 0:
            exit()
        elif menu == 1:
            user_check(connection)
        elif menu == 2:
            user_delete(connection)

# Function to display the parts editing menu for the EzPC program
# Admin can enter 0 to exit the program
# Admin can enter -1 to return to the admin menu
def menu_admin_parts(connection):
        menu = -1
        while menu != 0:
            menu = int(input("---PARTS EDITING MENU---\n[-1] BACK\n[0] EXIT\n[1] CHECK\n[2] DELETE\nSelect option: "))
            if menu == -1:
                return
            elif menu == 0:
                exit()
            elif menu == 1:
                parts_check(connection)
            elif menu == 2:
                parts_delete(connection)

# Function to check if the user exists in the database
# Admin can enter 0 to exit the program
# Admin can enter -1 to return to the admin menu
def user_check(connection):
    print("---CHECK USER---")
    print("Enter 0 to exit the program.")
    print("Enter -1 to return to the previous menu")
    while True:
        username = input("Enter username to check in the database: ")
        if username == "0":
            exit()
        if username == "-1":
            return
        cursor = connection.cursor()
        cursor.execute(check_username_query, (username,))

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
def user_delete(connection):
    print("---DELETE USER---")
    print("Enter 0 to exit the program.")
    print("Enter -1 to return to the previous menu")
    while True:
        username = input("Enter username to delete in the database: ")
        if username == "0":
            exit()
        if username == "-1":
            return
        
        # Check if user exists in the database
        cursor = connection.cursor()
        cursor.execute(check_username_query, (username,))
        result = cursor.fetchone()
        cursor.close()
        if not result:
            print("User does not exist in the database.")
        else:
            print("Are you sure you want to delete", username, "from the database?", end="")
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


def parts_check(connection):
    pass

def parts_delete(connection):
    pass

""""""

# Function to exit the program
def exit():
    print("Exiting program.")
    raise SystemExit