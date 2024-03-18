# models/user_model.py

import peewee
from utils.db import db

class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    username = peewee.CharField(unique=True, index=True)
    password = peewee.CharField()
    key = peewee.CharField(null=True)

    class Meta:
        database = db
