import asyncio
import logging

from config import rabbitmq_config, queue_name
from services.event_consumer import EventConsumer
from services.queue_client import init_rabbitmq_client_adapter


logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    queue_client = loop.run_until_complete(init_rabbitmq_client_adapter(rabbitmq_config))
    event_consumer = EventConsumer(queue_client, logger, queue_name)
    loop.run_until_complete(event_consumer.run())
    loop.run_forever()
