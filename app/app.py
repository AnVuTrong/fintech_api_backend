from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI(title="Fintech API backend")

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Fintech API backend"}