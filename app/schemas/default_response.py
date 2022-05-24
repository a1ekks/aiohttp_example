from marshmallow import Schema, fields


class DefaultResponseSchema(Schema):
    status = fields.Str()
