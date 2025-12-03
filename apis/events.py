from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.events import EventsRequest, EventsResponse
from service.events import events as events_service
from db import get_session
from repositories.events import Events
import json

router = APIRouter(prefix="/events")

@router.post("/", response_model=EventsResponse)
async def get_events(request: EventsRequest, session: AsyncSession = Depends(get_session)):
    rep = Events(session)
    return await events_service.get_events(request, rep)
