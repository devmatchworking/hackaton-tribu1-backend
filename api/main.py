from fastapi import FastAPI, HTTPException
from routes import letters
import uvicorn
import os
from dotenv import load_dotenv
from db.db import connect_and_init_db
load_dotenv()


app = FastAPI()
app.include_router(letters.router)

async def startup_event():
    connected = await connect_and_init_db()
    if not connected:
        raise HTTPException(status_code=500, detail="No se pudo conectar a MongoDB")
    else:
        print("Connection with DB Succesfull!")

app.add_event_handler("startup", startup_event)

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("HOST"),port=int(os.getenv("PORT")))