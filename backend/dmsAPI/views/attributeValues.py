import logging

from ninja import Router

from dmsAPI.schema.AttributesValueSchema import AttributesValueSchema
from dmsApp.service.AttributeService import AttributeService
from dmsApp.service.GeminiService import GeminiService
from dmsApp.service.PdfService import PdfService

attributeValuesRouter = Router()
logger = logging.getLogger(__name__)


@attributeValuesRouter.get("/{id}", tags=["AttributeValues"], summary="Get Attribute Values By Pdf",
                           response=list[AttributesValueSchema])
def getAttributeValuesByPdf(request, id: int):
    attributeService = AttributeService()
    return attributeService.getAttributesByPdf(id)


@attributeValuesRouter.get("/geminiValues/{id}", tags=["AttributeValues"],
                           summary="Get Attribute Values By Pdf from Gemini", response=list[str]
                           )
def getGeminiAttributeValuesByPdf(request, id):
    geminiService = GeminiService()
    #  geminiService.getAttributesByPdf(id)
    pdfService = PdfService()
    pdf = pdfService.getPdfById(id)
    geminiService.connect()
    geminiService.uploadFile(pdf.file.name)
    return geminiService.getAttributesByPdf(id)
