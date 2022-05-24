from dataclasses import dataclass
from enum import Enum


class EventType(Enum):
    TEST_EVENT_1 = 1
    TEST_EVENT_2 = 2

    @classmethod
    def list(cls):
        return [item.value for item in cls]


@dataclass
class Event:
    id: str
    name: str
    type: EventType


@dataclass
class ValidationObject:
    event: Event = None
    error: list = None
    src: dict = None
