from datetime import datetime
from typing import Optional

from dmsApp.models import Archive
from ninja import ModelSchema


class ArchiveSchema(ModelSchema):
    id: Optional[int] = None
    create_on: Optional[datetime] = None

    class Config:
        model = Archive
        model_fields = ["id", "create_on", "name"]
