from pydantic import BaseModel, Field


class EnterpriseInfo(BaseModel):
    name: str = Field(..., example="Matchworking")
    recipient: str = Field(..., example="Anthonio Doe")
    position: str = Field(..., example="Gerente RRHH")
    vacant: str = Field(..., example="Backend Developer")
    information: str = Field(...,
                             example="Dedicada al desarrollo de Servicios")
