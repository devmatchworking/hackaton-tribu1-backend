from pydantic import BaseModel, Field, EmailStr


class UserInfo(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., gt=0, lt=130)
    email: EmailStr = Field(..., example="johndoe@example.com")