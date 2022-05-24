from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec

from app.middlewares import setup_middlewares
from app.routes import setup_routes


def setup_app(queue_producer):
    app = web.Application()
    app['queue_producer'] = queue_producer

    setup_routes(app)
    setup_aiohttp_apispec(app, title='event-driven RestAPI', url='/schema', swagger_path='/docs')
    setup_middlewares(app)

    return app


def start_app(host, port, queue_producer):
    app = setup_app(queue_producer)
    web.run_app(app, host=host, port=port)
