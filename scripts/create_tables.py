from models.user_model import User

from utils.db import db

def create_tables():
    with db:
        db.create_tables([User])