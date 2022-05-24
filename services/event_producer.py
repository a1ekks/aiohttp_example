from services.internal_objects import ValidationObject, Event
from services.queue_client import QueueClientAbstract


class EventProducer:

    def __init__(self,
                 queue_client: QueueClientAbstract,
                 queue_name: str,
                 validation):

        self.validation = validation
        self.queue_name = queue_name
        self.queue_client = queue_client

    async def validate(self, data: dict) -> ValidationObject:
        try:
            event = Event(**data)
            validation_object = ValidationObject(event=event, error=[])
        except TypeError as _err:
            return ValidationObject(src=data, error=["Can't validate event"])
        return self.validation().handle(validation_object)

    async def produce(self, data):
        validation_result = await self.validate(data)
        if validation_result.error:
            return validation_result

        await self.queue_client.init_connection()
        await self.queue_client.send_to_queue(data, self.queue_name)
        await self.queue_client.close_connection()
        return validation_result
