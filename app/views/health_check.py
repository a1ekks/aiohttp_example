from aiohttp.web_response import json_response
from aiohttp_apispec import docs, response_schema

from app.schemas.default_response import DefaultResponseSchema


@docs(tags=['health_check'], summary='API status', description='Get current API status')
@response_schema(DefaultResponseSchema, 200)
async def health_check(request):
    return json_response({
        'status': 'OK',
        'headers': dict(request.headers)
    })
