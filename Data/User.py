"""
User.py
User class for user accounts
"""

from mongoengine import *
import datetime
from Data.Game import Game


class User(Document):
    user_id = ObjectIdField()
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    profile_picture = ImageField()
    comm_prefs = ListField(StringField())
    favorite_games = ListField(ReferenceField(Game))
    biography = StringField()
    creation_date = DateTimeField(default=datetime.datetime.now)
    friends = ListField(ReferenceField('self'))
    blocked = ListField(ReferenceField('self'))
    match_suggestions = ListField(ReferenceField('self'))


    meta = {
        'collection': 'User'
    }
