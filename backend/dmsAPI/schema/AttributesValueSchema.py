from datetime import datetime
from typing import Optional

from ninja import ModelSchema

from dmsAPI.schema.AttributesSchema import AttributesSchema
from dmsAPI.schema.PdfSchema import PdfSchema
from dmsApp.models import AttributesValue


class AttributesValueSchema(ModelSchema):
    id: Optional[int] = None
    createOn: Optional[datetime] = None
    attribute: AttributesSchema
    pdf: PdfSchema

    class Config:
        model = AttributesValue
        model_fields = ["value"]
