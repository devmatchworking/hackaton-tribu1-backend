from pydantic import BaseModel, Field, EmailStr


class UserInfo(BaseModel):
    name: str = Field(..., example="John Doe")
    vacant: str = Field(..., example="Backend Developer")
    enterprise: str = Field(..., example="Matchworking")
    experience: str = Field(...,
                            example="2 años Desarrollando API's con FastAPI")
