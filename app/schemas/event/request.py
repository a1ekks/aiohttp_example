

from enum import Enum

from marshmallow import Schema, fields, validate
#
#
# class EventType(Enum):
#     TEST_EVENT_1 = 1
#     TEST_EVENT_2 = 2
#
#     @classmethod
#     def list(cls):
#         return [item.value for item in cls]


class EventPost(Schema):

    id = fields.Str(required=True)
    name = fields.Str()
    type = fields.Integer(required=True)
    # type = fields.Integer(required=True, validate=validate.OneOf(EventType.list()))
