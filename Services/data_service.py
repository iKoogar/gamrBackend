"""
data_service.py
contains functions for accessing the mongo database
"""

import mongoengine
from Data.User import User
import json
from Data.Game import Game
from Data.Connection import Connection


# User stuff ==========================================================================================================


# takes a string for the email of the user to search for
# returns a tuple of the user and a boolean indicating if a user was found or not
def findUserByEmail(email: str):
    user = User()
    found = False
    if User.objects(email=email).count() > 0:
        user = User.objects(email=email).first()
        found = True
    return user, found

# searches for a user with the email 'eml'
# if the user is found and deleted, returns true
def deleteUserByEmail(eml: str):
    user, found = findUserByEmail(eml)
    if found:
        user.delete()
    return found


# creates a user with specified name, email, and password and saves them to the db
# returns the user object
def addUser(nam: str, eml: str, pwd: str) -> User:
    user = User()
    user.name = nam
    user.email = eml
    user.password = pwd
    # should check if email exists already
    user.save()
    return user

# returns all users in the database in json format
def getAllUsers():
    users = User.objects()

    return users.to_json()

# Game stuff ==========================================================================================================

