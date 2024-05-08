from pydantic import BaseModel, Field, EmailStr,BaseConfig
from models.letter import Letter
from bson import ObjectId
from models.letter import Letter


class Letter_DB(Letter):
    id: ObjectId = Field(..., example="6122a42e67a51d001555de9a")
    letter: Letter
    #date: 
    #user:

    class Config:
        arbitrary_types_allowed = True
    
    @classmethod
    def from_mongo(cls, data):
        return cls(**data)

    def to_mongo(self):
        return self.model_dump()