from fastapi import FastAPI

from routers.users_router import router as user_router

app = FastAPI()

app.include_router(user_router)