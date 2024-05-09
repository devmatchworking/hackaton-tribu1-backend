from db.db import get_db
from bson import ObjectId
from models.letter import Letter

async def update_letter_id(id: str, letter: Letter):
    try:
        db = await get_db()
        collection = db['letters']  
        
        result = await collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": letter}
        )

        if result.modified_count == 1:
            return result
        else:
            return None
        
    except Exception as e:
        print("Error al actualizar carta por ID:", e)
        return None
