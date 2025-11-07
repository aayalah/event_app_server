from pydantic import BaseModel 


class LoginRequest(BaseModel):
   user_name: str
   password: str 


class LoginResponse(BaseModel):
   token: str
   refresh_token: str