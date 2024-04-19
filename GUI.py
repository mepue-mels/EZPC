#!/usr/bin/env python3

from sql import create_server_connection
from sql import execute_query

class GUI:
    def __init__(self):
        self.setup()

    def getCredentials(self, username, password):
        username = input('Enter a username: ')

        while (username == "" or username == " "):
            username = input('invalid entry! please re-enter username: ')

        password = input('Enter password: ')
        while (password == "" or password == " "):
            username = input('invalid entry! please re-enter password: ')

        test_password = input('Re-enter your password: ')
        while test_password != password:
            test_password = input('Passwords do not match! Please re-enter: ')

    def setup(self):
        create_server_connection('localhost', 'root', 'Mar2022100306')

        selection = input("(1) Login\n(2) Register\n\nEnter selection: ")

        while (selection == "" or selection == " "):
            selection = input("Incorrect entry. Please re-enter selection: ")

        if (int(selection) == 1):
            self.login()
        elif (int(selection) == 2):
            self.register()
        else:
            print("Wrong selection.")

    def login(self):
        username = ""
        password = ""
        self.getCredentials(username,password)

    def register(self):
        username = ""
        password = ""
        self.getCredentials(username,password)






sample = GUI()
