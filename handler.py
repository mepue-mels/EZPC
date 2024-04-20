#!/usr/bin/env python3

from sql import execute_query
from user import User


class Handler:
    def __init__(self, User, connection):
        self.currentUser = User
        self.username, self.password = User.getCredentials()
        self.connection = connection

        if (self.username=="root" and self.password=="root"):
            self.isRoot = 1
        else:
            self.isRoot = 0

    def executeCommit(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        self.connection.commit()
        cursor.close()
        return result


    def checkUser(self, username, password):
        query = f'SELECT * FROM project.user_details WHERE username="{username}" AND password="{password}";'
        result = self.executeCommit(query)
        if result:
            return 1
        else:
            return 0

    def createUser(self, userObject):
        username, password = userObject.getCredentials()
        userExists = self.checkUser(username,password)

        if userExists:
            return 0
        else:
            query = f'INSERT INTO project.user_details (username, password) VALUES ("{username}", "{password}")'
            self.executeCommit(query)
            return 1
    def deleteUser(self, userObject):
        username, password = userObject.getCredentials()
        if not self.isRoot:
            return 0

        userExists = self.checkUser(username, password)

        if not userExists:
            return 0
        else:
            query = f'DELETE FROM project.user_details WHERE username="{username}" AND password="{password}"'
            self.executeCommit(query)
            return 1
