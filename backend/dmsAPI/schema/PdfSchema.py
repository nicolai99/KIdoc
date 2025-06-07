from typing import Optional

from ninja import Schema


class PdfSchema(Schema):
    id: Optional[int] = None
    name: str
    archive_id: int
