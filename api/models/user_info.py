from pydantic import BaseModel, Field, EmailStr

# The UserInfo class is a Pydantic model that represents the data that the user will provide in the request body.
# the atributes are used to generated a motivational letter


class UserInfo(BaseModel):
    name: str = Field(..., min_length=5, max_length=25, example="John")
    last_name: str = Field(..., example="Doe")
    email: EmailStr = Field(..., example="johndoe@example.com")
    contact: str = Field(..., min_length=10,
                         max_length=10, example="0910101010")
    experience: str = Field(..., min_length=25, max_length=200,
                            example="3 years in backend development at XYZ Company")

    # return a string with the prompt to be used in the openai api

    def get_as_prompt(self):
        return f"Nombre: {self.name}, Email: {self.email}, Vacante: {self.vacancy}, Empresa: {self.company}, Info Empresa: {self.companyInfo}, Experiencia: {self.experience}"
