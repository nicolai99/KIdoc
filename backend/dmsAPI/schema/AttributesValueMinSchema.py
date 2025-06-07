from ninja import Schema


class AttributesValueMinSchema(Schema):
    attribute_id: int
    value: str | int
