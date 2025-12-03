from schemas.users import CreateUserRequest, CreateUserResponse
from repositories.user import User
import bcrypt

async def create_user(user_request: CreateUserRequest, rep: User) -> CreateUserResponse:
    hashed = bcrypt.hashpw(user_request.password.encode(), bcrypt.gensalt())
    created_user = await rep.create(user_request.full_name, user_request.user_name, user_request.email, hashed.decode("utf-8"))  
    response = CreateUserResponse(id=created_user.id, full_name=created_user.full_name, email=created_user.email, user_name=created_user.user_name)
    return response
