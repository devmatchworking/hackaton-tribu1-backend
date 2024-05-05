from fastapi import APIRouter
from models.letter import Letter
from models.user_info import UserInfo

router = APIRouter(
    tags=["Letter Routes"]
)

@router.post("/letter", response_model=Letter, status_code=201)
async def create_letter(user_info: UserInfo):
    #TODO: Implement
    return {"message": "To implement"}