from ninja import ModelSchema

from dmsAPI.schema.AttributesValueMinSchema import AttributesValueMinSchema
from dmsApp.models import PDFDocument


class PdfWithValuesSchema(ModelSchema):
    attribute_values: list[AttributesValueMinSchema]

    class Meta:
        model = PDFDocument
        fields = "__all__"
