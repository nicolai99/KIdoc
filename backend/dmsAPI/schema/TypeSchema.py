from datetime import datetime
from typing import Optional

from ninja import ModelSchema

from dmsApp.models import Type
from ninja import ModelSchema


class TypeSchema(ModelSchema):
    id: Optional[int] = None
    createOn: Optional[datetime] = None
    name: Optional[str] = None

    class Config:
        model = Type
        model_fields = ["id", "createOn", "name"]
