from ninja import ModelSchema

from dmsAPI.schema.AttributesSchema import AttributesSchema
from dmsApp.models import AttributesValue


class AttributesValueMinSchema(ModelSchema):
    attribute: AttributesSchema

    class Meta:
        model = AttributesValue
        fields = "__all__"
