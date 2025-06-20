import logging

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ninja import File, Form
from ninja import Router
from ninja import Schema
from ninja.files import UploadedFile

from dmsAPI.schema.PdfWithValuesSchema import PdfWithValuesSchema
from dmsApp.models import PDFDocument, Archive
from dmsApp.service.PdfService import PdfService

logger = logging.getLogger(__name__)


class PdfUploadRequestSchema(Schema):
    archive_id: int


class ArchiveSchema(Schema):
    id: int
    name: str


pdfRouter = Router()


@pdfRouter.post("/upload", response={200: int}, tags=["Pdf"], summary="Upload a PDF file")
def upload_pdf(request, file: UploadedFile = File(...),
               data: PdfUploadRequestSchema = Form(...)):
    try:
        pdf_archive = get_object_or_404(Archive, id=data.archive_id)
    except Exception as e:
        raise Exception

    pdf_doc = PDFDocument(
        file=file,
        name=file.name,
        archive=pdf_archive
    )
    pdf_doc.save()
    return pdf_doc.id


@pdfRouter.get("/{pdf_id}", tags=["Pdf"], summary="Get PDF content")
def get_pdf_content(request, pdf_id: int):
    pdfService = PdfService()
    pdf_doc = pdfService.getPdfById(pdf_id)
    response = HttpResponse(pdf_doc.file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_doc.name or "document.pdf"}"'
    return response


@pdfRouter.delete("/delete/{pdf_id}", response={204: None}, tags=["Pdf"], summary="Delete PDF")
def delete_pdf(request, pdf_id: int):
    pdf_doc = get_object_or_404(PDFDocument, id=pdf_id)
    pdf_doc.delete()
    return HttpResponse(status=204)


@pdfRouter.post("/pdfSearch/{archiveId}", response=list[PdfWithValuesSchema], tags=["Pdf"],
                summary="List all Pdf by Seachparameter")
def pdfSearch(request, archiveId: int, search: list[str | int | None]):
    pdfService = PdfService()
    return pdfService.getPdfsBySearchValues(archiveId, search)
