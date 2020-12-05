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


def deleteUserByEmail(eml: str):
    user, found = findUserByEmail(eml)
    if found:
        print("found user with email :", eml,": deleting")
        user.delete()




def addUser(nam: str, eml: str, pwd: str) -> User:
    user = User()
    user.name = nam
    user.email = eml
    user.password = pwd
    # should check if email exists already
    user.save()
    return user


def getAllUsers():
    users = User.objects()

    return users.to_json()

# Game stuff ==========================================================================================================
