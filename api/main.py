from fastapi import FastAPI, HTTPException
from routes import letters
import uvicorn
import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from utils.check_db_conn import check_mongo_connection
from fastapi.middleware.cors import CORSMiddleware

from db.db import connect_and_init_db
load_dotenv()


app = FastAPI()
app.include_router(letters.router)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



mongo_uri = os.getenv("MONGODB_URL") 
client = AsyncIOMotorClient(mongo_uri)
db = client["letter_database"]

async def startup_event():
    connected = await connect_and_init_db()
    if not connected:
        raise HTTPException(status_code=500, detail="No se pudo conectar a MongoDB")
    else:
        print("Connection with DB Succesfull!")

app.add_event_handler("startup", startup_event)

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"),port=int(os.getenv("PORT")))