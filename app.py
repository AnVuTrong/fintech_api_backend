from fastapi import FastAPI
from sqlmodel import SQLModel
from app.db import engine
from app.api.routers import user_controllers

app = FastAPI()


def create_tables():
    SQLModel.metadata.create_all(engine)

app.include_router(user_controllers.router)
