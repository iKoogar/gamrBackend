from mongoengine import *


class Game(Document):
    name = StringField()
    is_multiplayer = BooleanField()
    players_matched = IntField()


    meta = {
        'collection': 'Game'
    }
