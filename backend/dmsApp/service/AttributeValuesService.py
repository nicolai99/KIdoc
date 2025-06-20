import logging

from dmsApp.models import AttributesValue
from dmsApp.service.ArchiveService import ArchiveService
from dmsApp.service.PdfService import PdfService


class AttributeValuesService:
    logger = logging.getLogger(__name__)
    pdfService = PdfService()
    archiveService = ArchiveService()

    def getAttributesByPdf(self, id: int):
        _pdf = self.pdfService.getPdfById(id)
        return AttributesValue.objects.filter(pdf=_pdf).all()

    def setAttributeValues(self, id: int, values: list):
        pdf = self.pdfService.getPdfById(id)
        archive = self.archiveService.getArchiveById(pdf.archive_id)
        attributeValues = self.getAttributesByPdf(id)
        if attributeValues:
            attributeValues.delete()
        index = 0
        for att in archive.attributes.all():
            AttributesValue.objects.create(pdf=pdf, attribute=att, value=values[index])
            index += 1
        return None
