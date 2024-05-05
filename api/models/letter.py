from pydantic import BaseModel, Field, EmailStr


class Letter(BaseModel):
    content: str = Field(..., example="The content of the letter")