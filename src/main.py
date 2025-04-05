from fastapi import FastAPI
from routes import raspberry_awards
import database.database
import uvicorn

app = FastAPI()
app.include_router(raspberry_awards.router)


if __name__ == "__main__":
    database.database.init("resources/movielist.csv")
    print(database.database.get_dados())
    uvicorn.run(app, host="0.0.0.0", port=8000)