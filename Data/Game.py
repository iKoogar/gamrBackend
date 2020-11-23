from mongoengine import *


class Game(Document):
    name = StringField()
    isMultiplayer = BooleanField()
    playersMatched = IntField()


    meta = {
        'collection': 'Game'
    }
