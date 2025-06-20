from ninja import ModelSchema

from dmsApp.models import AttributesValue


class AttributesValueValueSchema(ModelSchema):
    class Meta:
        model = AttributesValue
        fields = ["value"]
