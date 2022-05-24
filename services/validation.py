from abc import ABC, abstractmethod
from logging import Logger
from typing import Optional

from services.internal_objects import ValidationObject, EventType


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[ValidationObject]:
        pass


class BaseValidatorHandler(Handler):

    def __init__(self):
        self._next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, handler_object: ValidationObject) -> ValidationObject:
        if self._next_handler:
            return self._next_handler.handle(handler_object)
        else:
            return handler_object


class EventTypeChainValidator(BaseValidatorHandler):
    def handle(self, validation_object: ValidationObject) -> ValidationObject:
        if validation_object.event.type not in EventType.list():
            error_message: str = f'EventType: {validation_object.event.type} is not acceptable!'
            validation_object.error.append(error_message)

        return super().handle(validation_object)


def validation_chain() -> BaseValidatorHandler:
    event_type_validator = EventTypeChainValidator()

    return event_type_validator
