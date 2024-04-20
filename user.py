#!/usr/bin/env python3

class User:
    def __init__(self):
        self.username = ""
        self.password = ""

    def setUsername(self, u):
        self.username = u

    def setPassword(self, p):
        self.password = p

    def setCredentials(self, u, p):
        self.setUsername(u)
        self.setPassword(p)

    def getCredentials(self):
        return self.username, self.password

    def printCredentials(self):
        print( self.getUsername() )
        print( self.getPassword() )

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password



