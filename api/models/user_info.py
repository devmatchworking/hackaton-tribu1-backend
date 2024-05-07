from pydantic import BaseModel, Field, EmailStr

# The UserInfo class is a Pydantic model that represents the data that the user will provide in the request body.
# the atributes are used to generated a motivational letter
class UserInfo(BaseModel):
    name: str = Field(..., min_length=5,max_length=25, example="John Doe")
    age: int = Field(..., gt=0, lt=130,example=19)
    email: EmailStr = Field(..., example="johndoe@example.com")
    vacancy: str = Field(..., min_length=5,max_length=50, example="Software Engineer")
    company: str = Field(...,  min_length=5,max_length=25,example="ABC Company")
    companyInfo: str = Field(...,  min_length=25,max_length=200, example="ABC Company is a leading tech company in the industry")
    experience: str = Field(..., min_length=25,max_length=200, example="3 years in backend development at XYZ Company")
    
