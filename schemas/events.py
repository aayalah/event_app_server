from pydantic import BaseModel 


class EventsRequest(BaseModel):
    category: str
    latitude: float
    longitude: float
    radius: float

class Event(BaseModel):
    id: int
    name: str
    url: str
    categories: list[str]   
    venueName: str
    venuePostalCode: str
    venueCountry: str
    venueStateName: str
    venueStateCode: str
    venueCityName: str
    venueAddressLine1: str
    venueAddressLine2: str

class EventsResponse(BaseModel):
    events: list[Event]

