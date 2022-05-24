from aiohttp.web_app import Application
from aiohttp_apispec import validation_middleware


def setup_middlewares(app: Application):
    app.middlewares.append(validation_middleware)
