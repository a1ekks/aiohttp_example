import json
import logging

from services.queue_client import QueueClientAbstract


class EventConsumer:

    def __init__(self,
                 queue_client: QueueClientAbstract,
                 logger: logging.Logger,
                 queue_name: str):

        self.queue_name = queue_name
        self.logger = logger
        self.queue_client = queue_client

    async def on_message(self, queue_message, ack=False):
        message: dict = json.loads(queue_message.body.decode())
        if ack:
            await queue_message.channel.basic_ack(queue_message.delivery.delivery_tag)

        self.logger.info(f'New message: {message}')

    async def run(self):
        await self.queue_client.get_awaiting_from_queue(self.queue_name, self.on_message)
