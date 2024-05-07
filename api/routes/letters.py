from fastapi import APIRouter
from services.get_openai_response import get_openai_response
from services.db.get_letter_by_id import find_letter_id
from services.db.create_letter import create_letter_db
from models.letter import Letter
from models.user_info import UserInfo


router = APIRouter(
    tags=["Letter Routes"]
)

@router.post("/letter", response_model=Letter, status_code=201)
async def create_letter(user_info: UserInfo):
    content = get_openai_response(user_info.get_as_prompt()) 
    letter = Letter(content=content)
    #await create_letter_db(letter)
    return letter

@router.get('/letter/{id}')
async def get_letter(id: str):
    find_letter = find_letter_id(id) #todo: implementar busqueda por id en BD de carta generada
    if (find_letter):
        letter = Letter(content=find_letter.content)
        return letter
    else:
        return {"message": "Carta no encontrada"}