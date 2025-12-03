from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_
from models.events import Event as Event_Model
from geoalchemy2.functions import ST_Distance_Sphere 
from geoalchemy2 import Geometry

class Events:
    def __init__(self, db: AsyncSession):
        self.db = db 

    async def get(self, category: str, latitude: float, longitude: float, radius: float) -> list[Event_Model]:
        stmt = select(Event_Model).where(ST_Distance_Sphere(Event_Model.location, Geometry(x=longitude, y=latitude, srid=4326)) < radius).filter(Event_Model.categories.contains([category]))
        result =  await self.db.execute(stmt)
        events = result.scalars().all()
        return events