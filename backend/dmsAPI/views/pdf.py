from ninja import Router
from ninja import File, Form
from ninja.files import UploadedFile
from dmsApp.models import PDFDocument, Archive
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ninja import Schema
from typing import List
from ninja.security import django_auth
from dmsAPI.schema.PdfSchema import PdfSchema

class PdfUploadRequestSchema(Schema):
    archive_id: int

class ArchiveSchema(Schema):
    id: int
    name: str

pdfRouter = Router()

@pdfRouter.post("/upload", response={200: PdfSchema}, auth=django_auth)
def upload_pdf(request, file: UploadedFile = File(...),
               data: PdfUploadRequestSchema = Form(...)):
    file_data = file.read()

    try:
        pdf_archive = get_object_or_404(Archive, id=data.archive_id)
    except Exception as e:
        raise e

    pdf_doc = PDFDocument(
        file=file_data,
        name=file.name,
        archive=pdf_archive
    )
    pdf_doc.save()
    return {
        "id": pdf_doc.id,
        "name": pdf_doc.name,
        "content_url": request.build_absolute_uri(f"/api/upload/pdfs/{pdf_doc.id}/"),
        "archive_id": pdf_doc.archive.id
    }


@pdfRouter.get("/files", response=List[PdfSchema], auth=django_auth)
def list_pdfs(request):
    pdfs = PDFDocument.objects.all()
    return [
        {
            "id": pdf.id,
            "name": pdf.name,
            "content_url": request.build_absolute_uri(f"/api/upload/pdfs/{pdf.id}/"),
            "archive_id": pdf.archive.id
        }
        for pdf in pdfs
    ]


@pdfRouter.get("/pdfs/{pdf_id}/", auth=None)
def get_pdf_content(request, pdf_id: int):
    pdf_doc = get_object_or_404(PDFDocument, id=pdf_id)
    response = HttpResponse(pdf_doc.file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_doc.name or "document.pdf"}"'
    return response


@pdfRouter.delete("/pdfs/{pdf_id}/", response={204: None}, auth=django_auth)
def delete_pdf(request, pdf_id: int):
    pdf_doc = get_object_or_404(PDFDocument, id=pdf_id)
    pdf_doc.delete()
    return HttpResponse(status=204)

@pdfRouter.get("/archives", response=List[ArchiveSchema], auth=django_auth)
def list_archives(request):
    archives = Archive.objects.all()
    return [
        {"id": archive.id, "name": archive.name}
        for archive in archives
    ]
