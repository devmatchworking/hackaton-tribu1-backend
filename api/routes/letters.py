from fastapi import APIRouter
from services.get_openai_response import get_openai_response
from services.db.get_letter_by_id import find_letter_id
from services.db.create_letter import create_letter_db
from models.letter import Letter
from models.letter_db import Letter_DB
from models.user_info import UserInfo


router = APIRouter(
    tags=["Letter Routes"]
)

@router.post("/letter", response_model=Letter, status_code=201)
async def create_letter(user_info: UserInfo):
    content = get_openai_response(user_info.get_as_prompt()) 
    letter = Letter(content=content)
    return letter

@router.post("/letter-db", response_model=Letter_DB, status_code=201)
async def save_letter(letter: Letter):
    await create_letter_db(letter)
    return letter

@router.get('/letter-db/{id}',response_model=Letter_DB, status_code=201)
async def get_letter(id: str):
    find_letter = await find_letter_id(id)
    if find_letter:
        # Convertir ObjectId a str
        letter_db = Letter_DB(id=str(find_letter["_id"]), letter=Letter(content=find_letter["content"]))
        return letter_db
    else:
        return {"message": "Carta no encontrada"}