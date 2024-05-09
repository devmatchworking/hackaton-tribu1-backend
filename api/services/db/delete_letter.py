from ...db.db import get_db
from bson import ObjectId

async def delete_letter_id(id: str):
    try:
        db = await get_db()
        collection = db['letters']  


        result = await collection.delete_one({"_id": ObjectId(id)})
        
        if result.deleted_count == 1:
            return True 
        else:
            return False 

    except Exception as e:
        print("Error al eliminar carta por ID:", e)
        return None
