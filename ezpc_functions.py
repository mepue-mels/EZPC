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
def user_insert(connection):
    count = 0
    while True:
        count += 1
        print("---REGISTER---")
        username = input("Enter username: ")
        password = input("Enter password: ")

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
def user_login(connection):
    print("---LOGIN---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Execute a SELECT query to check if the username and password combination exists
    cursor = connection.cursor()
    cursor.execute(verify_login_query, (username, password))

    # Check if any rows were returned
    result = cursor.fetchone()
    if result[1] == "root":
        print("Admin access granted.")
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
# The admin menu can only be accessed by the "root" user
# The admin menu can be used to check and delete users from the database
def menu_admin(connection):
    menu = -1
    while menu != 0:
        menu = int(input("---ADMIN MENU---\n[0] EXIT\n[1] USERS\n[2] PARTS (x)\nSelect option: "))
        if menu == 0:
            exit()
        elif menu == 1:
            menu_admin_user()

# Function to display the user editing menu for the EzPC program
def menu_admin_user(connection):
    menu = -1
    while menu != 0:
        menu = int(input("---USER EDITING MENU---\n[0] EXIT\n[1] CHECK \n[2] DELETE (x)\nSelect option: "))
        if menu == 0:
            exit()
        elif menu == 1:
            user_check(connection)

def user_check(connection):
    pass

""""""

# Function to exit the program
def exit():
    print("Exiting program.")
    raise SystemExit