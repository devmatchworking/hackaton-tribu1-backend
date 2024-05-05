from fastapi import FastAPI
from routes import letters
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()


app = FastAPI()
app.include_router(letters.router)


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"),port=int(os.getenv("PORT")))