from pydantic import BaseModel

class UpdateLetterRequest(BaseModel):
    content: str
