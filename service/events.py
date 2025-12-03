from schemas.events import EventsRequest, EventsResponse, Event
from repositories.events import Events

async def get_events(events_request: EventsRequest, rep: Events) -> EventsResponse:
    events = await rep.get(events_request.category, events_request.latitude, events_request.longitude, events_request.radius)
    events_response = EventsResponse(events=[])
    for event in events:
        events_response.events.append(Event(id=event.id, name=event.name, url=event.url, categories=event.categories, venueName=event.venueName, venuePostalCode=event.venuePostalCode, venueCountry=event.venueCountry, venueStateName=event.venueStateName, venueStateCode=event.venueStateCode, venueCityName=event.venueCityName, venueAddressLine1=event.venueAddressLine1, venueAddressLine2=event.venueAddressLine2))
    return events_response