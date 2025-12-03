from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float
from sqlalchemy.dialects.postgresql import JSONB
from GeoAlchemy2 import Geometry
class Event(Base):
    __tablename__ = "events"
    id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column(String(30))
    name: Mapped[str] = mapped_column(String(30))
    url: Mapped[str] = mapped_column(String(30))
    categories: Mapped[list[str]] = mapped_column(JSONB)
    venueName: Mapped[str] = mapped_column(String(30))
    location: Mapped[Geometry] = mapped_column(Geometry(geometry_type='POINT', srid=4326))
    venuePostalCode: Mapped[str] = mapped_column(String(30))
    venueCountry: Mapped[str] = mapped_column(String(30))
    venueStateName: Mapped[str] = mapped_column(String(30))
    venueStateCode: Mapped[str] = mapped_column(String(30))
    venueCityName: Mapped[str] = mapped_column(String(30))
    venueAddressLine1: Mapped[str] = mapped_column(String(30))
    venueAddressLine2: Mapped[str] = mapped_column(String(30))

