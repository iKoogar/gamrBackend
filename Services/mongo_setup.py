"""
mongo_setup.py
connects to a remote mongodb server using credentials within a dictionary called 'secrets'
"""

import mongoengine

def global_init(secrets):
    mongoengine.connect(db=secrets["db"], username=secrets["username"], password=secrets["password"],
                        host=secrets["host"], name="gamr")