import logging

from ninja import Router

from dmsAPI.schema.AttributesValueSchema import AttributesValueSchema
from dmsApp.service.AttributeValuesService import AttributeValuesService
from dmsApp.service.GeminiService import GeminiService
from dmsApp.service.PdfService import PdfService

attributeValuesRouter = Router()
logger = logging.getLogger(__name__)


@attributeValuesRouter.get("/list/{id}", tags=["AttributeValues"], summary="Get Attribute Values By Pdf",
                           response=list[AttributesValueSchema])
def getAttributeValuesByPdf(request, id: int):
    attributeValuesService = AttributeValuesService()
    return attributeValuesService.getAttributesByPdf(id)


@attributeValuesRouter.get("/listValues/{id}", tags=["AttributeValues"], summary="Get Attribute Values By Pdf",
                           response=list[str | int | None | float])
def getAttributeValuesMinByPdf(request, id: int):
    attributeValuesService = AttributeValuesService()
    attributeValues = attributeValuesService.getAttributesByPdf(id)
    listAtt = attributeValues.values_list('value', flat=True)
    return listAtt


@attributeValuesRouter.post("/{id}", tags=["AttributeValues"], summary="Set Attribute Values By Pdf",
                            )
def setAttributeValuesByPdf(request, id: int, values: list[str | int | None]):
    attributeValuesService = AttributeValuesService()
    return attributeValuesService.setAttributeValues(id, values)


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
