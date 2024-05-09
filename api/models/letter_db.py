from bson import ObjectId
from .letter import Letter
from pydantic import BaseModel, Field, field_validator, ValidationError


class Letter_DB(BaseModel):
    id: str = Field(..., example="6122a42e67a51d001555de9a")
    letter: Letter

    @field_validator('id')
    def validate_object_id(cls, v):
        try:
            ObjectId(v)
        except Exception:
            raise ValueError('Invalid ObjectId')
        return v

    letter: Letter
    
    @classmethod
    def from_mongo(cls, data):
        return cls(id=str(data["_id"]), letter=Letter(content=data["content"]))

    def to_mongo(self):
        return self.model_dump()