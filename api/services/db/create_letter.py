

from db.db import get_db
async def create_letter_db(letter):
    try:
        db = await get_db()
        collection = db['letters']  
        result = await collection.insert_one(letter.dict())
        print("Elemento insertado correctamente en la base de datos:", result.inserted_id)
    except Exception as e:
        print("Error al escribir en la base de datos:", e)