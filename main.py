from typing import Union
from routers import users
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"inicio": "de la app"}