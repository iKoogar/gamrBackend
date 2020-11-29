from mongoengine import *
import datetime
from Data.Game import Game


class User(Document):
    user_id = ObjectIdField()
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
    profilePicture = ImageField()
    commPrefs = ListField(BooleanField())
    favoriteGames = ListField(ReferenceField(Game))
    biography = StringField()
    creation_date = DateTimeField(default=datetime.datetime.now)
    friends = ListField(ReferenceField('self'))  # idk
    blocked = ListField(ReferenceField('self'))  # idk
    matchSuggestions = ListField(ReferenceField('self'))  # idk


    meta = {
        'collection': 'User'
    }
