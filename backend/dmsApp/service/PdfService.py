from dmsAPI.ProcessingError import ProcessingError
from dmsApp.models import PDFDocument


class PdfService:
    def getPdfById(self, id: int):
        try:
            return PDFDocument.objects.get(id=id)
        except PDFDocument.DoesNotExist:
            raise ProcessingError("PDF does not exist", 1)
