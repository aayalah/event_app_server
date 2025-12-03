from pydantic import BaseModel 


class CreateUserRequest(BaseModel):
   user_name: str
   full_name: str
   email: str
   password: str 


class CreateUserResponse(BaseModel):
   id: int
   full_name: str
   email: str
   user_name: str