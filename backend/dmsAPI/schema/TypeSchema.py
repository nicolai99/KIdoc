from datetime import datetime
from typing import Optional

from ninja import ModelSchema

from dmsApp.models import Type


class TypeSchema(ModelSchema):
    id: Optional[int] = None
    createOn: Optional[datetime] = None
    name: Optional[str] = None

    class Config:
        model = Type
        model_fields = "__all__"
