"""
Game.py
Game class for games that people play
"""

from mongoengine import *


class Game(Document):
    name = StringField()
    is_multiplayer = BooleanField()
    players_matched = IntField()


    meta = {
        'collection': 'Game'
    }
