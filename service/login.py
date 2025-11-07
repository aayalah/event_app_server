from schemas.login import LoginRequest, LoginResponse
from repositories.user import User
async def login(request: LoginRequest, user_rep: User) -> LoginResponse:
    user = await user_rep.get(request.user_name, request.password)
    print(user)
    response = LoginResponse(token=user.user_name, refresh_token=user.password)
    return response