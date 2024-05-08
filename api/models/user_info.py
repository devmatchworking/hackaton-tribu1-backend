from pydantic import BaseModel, Field, EmailStr


class UserInfo(BaseModel):
    name: str = Field(..., example="John Doe")
    apellido: str = Field(..., example="Backend Developer")
    email: EmailStr = Field(..., example="example@expamle.com")
    contact: str = Field(..., example="0901010101")
    experience: str = Field(..., example="Ninguna")
