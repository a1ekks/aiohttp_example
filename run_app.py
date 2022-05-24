from app.app import start_app
from config import host, port, rabbitmq_config, queue_name
from services.event_producer import EventProducer
from services.queue_client import RabbitMqQueueClient, RabbitMqConfig
from services.validation import validation_chain


if __name__ == '__main__':
    queue_client = RabbitMqQueueClient(RabbitMqConfig(**rabbitmq_config), loop=None)
    queue_producer = EventProducer(queue_client, queue_name, validation=validation_chain)

    start_app(host=host, port=port, queue_producer=queue_producer)
