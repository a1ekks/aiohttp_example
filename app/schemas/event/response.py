from marshmallow import Schema, fields


class EventResponseOk(Schema):
    status = fields.Str()


class EventResponseFailed(Schema):
    status = fields.Str()
