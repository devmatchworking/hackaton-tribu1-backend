from pydantic import BaseModel, Field, EmailStr

# The UserInfo class is a Pydantic model that represents the data that the user will provide in the request body.
# the atributes are used to generated a motivational letter
class UserInfo(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., gt=0, lt=130,example=19)
    email: EmailStr = Field(..., example="johndoe@example.com")
    vacancy: str = Field(..., example="Software Engineer")
    company: str = Field(..., example="ABC Company")
    companyInfo: str = Field(..., example="ABC Company is a leading tech company in the industry")
    experience: str = Field(..., example="3 years in backend development at XYZ Company")
    

