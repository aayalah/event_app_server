from schemas.login import LoginRequest, LoginResponse
from repositories.user import User
import bcrypt

async def login(request: LoginRequest, user_rep: User) -> LoginResponse:
    user = await user_rep.get(request.email)
    user_pwd = request.password.encode('utf-8');
    stored_pwd = user.password_hash.encode('utf-8');
    if bcrypt.checkpw(user_pwd, stored_pwd):
        return LoginResponse(email=user.email, user_name=user.user_name, full_name=user.full_name)
