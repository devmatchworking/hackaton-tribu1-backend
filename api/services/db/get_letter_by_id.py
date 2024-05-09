from ...db.db import get_db
from bson import ObjectId

async def find_letter_id(id: str):
    try:
        db = await get_db()
        collection = db['letters']  

        letter = await collection.find_one({"_id": ObjectId(id)})

        return letter
    except Exception as e:
        print("Error al buscar carta por ID:", e)
        return None
