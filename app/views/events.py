from aiohttp.web_response import json_response
from aiohttp_apispec import docs, request_schema, response_schema

from app.schemas.event.request import EventPost
from app.schemas.event.response import EventResponseOk


@docs(tags=['events'], summary='Post new events', description='Post new event')
@request_schema(EventPost)
@response_schema(EventResponseOk, 200)
async def add_event(request):
    event_producer = request.app['queue_producer']
    data = await request.json()
    data.update({'name': request.url.parts[-1]})
    producer_result = await event_producer.produce(data)

    if producer_result.error:
        return json_response({'status': 'Failed', 'error': producer_result.error}, status=404)

    return json_response({'status': 'Ok'})
