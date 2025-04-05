from fastapi import FastAPI
from routes import raspberry_awards
import database.database
import uvicorn


database.database.init("resources/movielist.csv")
app = FastAPI()
app.include_router(raspberry_awards.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)