from Data.User import User
from Data.Game import Game
from Data.Connection import Connection


# User stuff ==========================================================================================================


def createUser(name: str, email: str, pwd: str) -> User:
    user = User()
    user.name = name
    user.email = email
    user.password = pwd

    user.save()
    return user


def find_user_by_email(email: str) -> User:
    user = User.objects(email=email).first()
    print("found user : ", user.name)
    return user


