from fastapi import FastAPI
from app.api.v1 import endpoints

app = FastAPI(title="Spam Detection API")

app.include_router(endpoints.router, prefix="/api/v1")
@app.get("/")
def read_root():
    return {"message": "Welcome to the Spam Classifier API"}