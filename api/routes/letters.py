from fastapi import APIRouter
from services.get_openai_response import get_openai_response
from models.letter import Letter
from models.user_info import UserInfo

router = APIRouter(
    tags=["Letter Routes"]
)

@router.post("/letter", response_model=Letter, status_code=201)
async def create_letter(user_info: UserInfo):
    content = get_openai_response(user_info.get_as_prompt()) # todo:pasar prompt
    letter = Letter(content=content)
    return letter