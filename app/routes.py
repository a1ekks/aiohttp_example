from aiohttp.web_app import Application

from app.views.events import add_event
from app.views.health_check import health_check


def setup_routes(app: Application):
    app.router.add_get('/healthcheck', health_check)
    app.router.add_post('/event/{name}', add_event)
