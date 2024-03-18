from fastapi import HTTPException, status

from passlib.context import CryptContext

from models.user_model import User as UserModel
from schema import user_schema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_data_hash(password):
    return pwd_context.hash(password)

def create_user(user: user_schema.UserRegister):

    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_data_hash(user.password),
        key = get_data_hash(user.key)
    )

    db_user.save()

    return user_schema.User(
        id = db_user.id,
        username = db_user.username,
        email = db_user.email,
        key = db_user.key
    )