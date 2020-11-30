from mongoengine import *
from Data.User import User
from Data.Game import Game


class Connection(Document):
    player1 = ReferenceField(User)
    player2 = ReferenceField(User)
    common_games = ListField(Game)


    meta = {
        'collection': 'Users'
    }
