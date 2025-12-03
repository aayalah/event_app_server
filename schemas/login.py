from pydantic import BaseModel 


class LoginRequest(BaseModel):
   email: str
   password: str 


class LoginResponse(BaseModel):
   user_name: str
   email: str
   full_name: str