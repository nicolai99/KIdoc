from datetime import datetime
from typing import Optional

from ninja import ModelSchema

from dmsAPI.schema.TypeSchema import TypeSchema
from dmsApp.models import Attribute


class AttributesSchema(ModelSchema):
    id: Optional[int] = None
    createOn: Optional[datetime] = None
    archive_id: Optional[int] = None
    type: TypeSchema

    class Config:
        model = Attribute
        model_fields = ["name", "label", "type"]
