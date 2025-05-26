from ninja import Schema

class PdfSchema(Schema):
    id: int
    name: str
    content_url: str