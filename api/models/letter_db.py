from pydantic import BaseModel, Field, EmailStr,BaseConfig
from models.letter import Letter
from bson import ObjectId

class Letter_DB(BaseModel):
    class Config(BaseConfig):
        arbitrary_types_allowed = True
    id: ObjectId
    letter: Letter
    #date: 
    #user: