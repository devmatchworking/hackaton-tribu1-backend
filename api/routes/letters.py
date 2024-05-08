import pymongo
from typing import Union
from fastapi import APIRouter
from services.get_openai_response import get_openai_response
from services.db.get_letter_by_id import find_letter_id
from services.db.create_letter import create_letter_db
from services.db.update_letter import update_letter_id
from services.db.delete_letter import delete_letter_id
from models.letter import Letter
from models.letter_db import Letter_DB
from models.user_info import UserInfo
from models.request_data import UpdateLetterRequest


router = APIRouter(
    tags=["Letter Routes"]
)

@router.post("/letter", response_model=Letter, status_code=201)
async def create_letter(user_info: UserInfo):
    content = get_openai_response(user_info.get_as_prompt()) 
    letter = Letter(content=content)
    return letter

#enviar cuerpo de request como {"content":"contenido de la carta"}
@router.post("/letter-db", response_model=Letter_DB, status_code=201)
async def save_letter(letter: Letter):
    letter_tmp = await create_letter_db(letter)

    if isinstance(letter_tmp, pymongo.results.InsertOneResult):
        letter_id = letter_tmp.inserted_id
        letter_tmp = await find_letter_id(letter_id)
        
    letter_db = Letter_DB(id=str(letter_tmp["_id"]), letter=Letter(content=letter_tmp["content"]))
    return letter_db

@router.get('/letter-db/{id}',response_model=Union[Letter_DB, dict], status_code=201)
async def get_letter(id: str):
    find_letter = await find_letter_id(id)
    if find_letter:
        letter_db = Letter_DB(id=str(find_letter["_id"]), letter=Letter(content=find_letter["content"]))
        return letter_db
    else:
        return {"message": "Carta no encontrada"}
    
#enviar cuerpo de request como {"content":"contenido de la carta"}
@router.put('/letter-db/{id}',response_model=Union[Letter_DB, dict], status_code=201)
async def update_letter(id: str, request: UpdateLetterRequest):
    letter_to_update = await find_letter_id(id)
    if letter_to_update:
        letter_to_update['content'] = request.content
        letter_db = await update_letter_id(id,letter_to_update)
        letter_db = Letter_DB(id=str(letter_to_update["_id"]), letter=Letter(content=letter_to_update["content"]))
        return letter_db
    else:
        return {"message": "Carta no encontrada"}

@router.delete('/letter-db/{id}',response_model=dict, status_code=201)
async def update_letter(id: str):
    letter_to_delete = await find_letter_id(id)
    if letter_to_delete:
        await delete_letter_id(id)
        return {"message": "Carta eliminada exitosamente"}
    else:
        return {"message": "Carta no encontrada"}
