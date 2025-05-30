from datetime import datetime
from typing import Optional, List

from ninja import ModelSchema

from dmsAPI.schema.AttributesSchema import AttributesSchema
from dmsApp.models import Archive


class ArchiveSchema(ModelSchema):
    id: Optional[int] = None
    createOn: Optional[datetime] = None
    attributes: Optional[List[AttributesSchema]] = None

    class Config:
        model = Archive
        model_fields = "__all__"
