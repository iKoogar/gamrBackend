from Data.User import User
from Data.Game import Game
from Data.Connection import Connection


# User stuff ==========================================================================================================


def createUser(nam: str, eml: str, pwd: str) -> User:
    user = User()
    user.name = nam
    user.email = eml
    user.password = pwd

    user.save()
    return user


def findUserByEmail(email: str) -> User:
    user = User.objects(email=email).first()
    print("found user : ", user.name)
    
    return user


def addUser(nam: str, eml: str, pwd: str) -> User:
    user = User()
    user.name = nam
    user.email = eml
    user.password = pwd

    user.save()
    return user


def getAllUsers():
    users = User.objects()

    return users.tojson()

