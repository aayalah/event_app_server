from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.login import LoginRequest, LoginResponse
from service.login import login as login_service
from db import get_session
from repositories.user import User
import json

router = APIRouter(prefix="/login")

@router.post("/", response_model=LoginResponse)
async def login(request: LoginRequest, session: AsyncSession = Depends(get_session)):
    rep = User(session)
    return await login_service(request, rep)
