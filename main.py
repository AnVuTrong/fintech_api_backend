from fastapi import FastAPI
from sqlmodel import SQLModel
from blog.database import engine
from blog.routers import blog, user, authentication

app = FastAPI()


def create_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
async def on_startup():
    create_tables()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)