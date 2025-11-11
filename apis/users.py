from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.users import CreateUserRequest, CreateUserResponse
from service.users import create_user as create_user_service
from db import get_session
from repositories.user import User
import json

router = APIRouter(prefix="/users")

@router.post("/", response_model=CreateUserResponse)
async def create_user(request: CreateUserRequest, session: AsyncSession = Depends(get_session)):
    rep = User(session)
    return await create_user_service(request, rep)
