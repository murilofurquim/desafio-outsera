import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.routes import raspberry_awards
from src.database import database
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    database.init(movies_csv='resources/movielist.csv')
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(raspberry_awards.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)