from ...db.db import get_db
async def create_letter_db(letter):
    try:
        db = await get_db()
        collection = db['letters']  
        letter = await collection.insert_one(letter.dict())
        return letter

    except Exception as e:
        print("Error al escribir en la base de datos:", e)
        return None
        