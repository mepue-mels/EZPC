#!/usr/bin/env python3

from sql import create_server_connection
from user import User
from handler import Handler

class Controller:
    def __init__(self):
        self.currentUser = User()
        self.conn = create_server_connection('localhost', 'root', 'Mar2022100306')
        self.modelHandler = None
        self.setup()

    def getCredentials(self, username=None, password=None):
        username = input('Enter a username: ')

        while (username == "" or username == " "):
            username = input('invalid entry! please re-enter username: ')

        password = input('Enter password: ')
        while (password == "" or password == " "):
            username = input('invalid entry! please re-enter password: ')

        test_password = input('Re-enter your password: ')
        while test_password != password:
            test_password = input('Passwords do not match! Please re-enter: ')

        return username, password

    def getLogin(self, username=None, password=None):
        username = input('Enter a username: ')

        while (username == "" or username == " "):
            username = input('invalid entry! please re-enter username: ')

        password = input('Enter password: ')
        while (password == "" or password == " "):
            username = input('invalid entry! please re-enter password: ')

        return username, password

    def setHandler(self):
        self.modelHandler = Handler(self.currentUser, self.conn)

    def userExists(self):
        return self.modelHandler.checkUser(self.currentUser.getUsername(), self.currentUser.getPassword())

    def setup(self):
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
        username, password = self.getLogin()
        self.currentUser.setCredentials(username, password)
        self.setHandler()

        if (self.userExists()):
            self.main()
        else:
            print("Incorrect login!")

    def register(self):
        username, password = self.getCredentials()
        self.currentUser.setCredentials(username, password)
        self.setHandler()
        createUser = self.modelHandler.createUser(self.currentUser)

        if createUser:
            self.main()
        else:
            print("user already existing!")

    def main(self):
        print("success")
