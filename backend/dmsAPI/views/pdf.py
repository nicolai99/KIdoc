from ninja import Router
from ninja import File
from ninja.files import UploadedFile
from dmsApp.models import PDFDocument
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ninja import Schema
from typing import List, Optional
from ninja.security import django_auth
from dmsAPI.schema.PdfSchema import PdfSchema

pdfRouter = Router()

@pdfRouter.post("/upload", response={200: PdfSchema}, auth=django_auth)
def upload_pdf(request, file: UploadedFile = File(...)):
    file_data = file.read()
    pdf_doc = PDFDocument(
        file_content=file_data,
        name=file.name,
    )
    pdf_doc.save()
    return {
        "id": pdf_doc.id,
        "name": pdf_doc.name,
        "content_url": request.build_absolute_uri(f"/api/upload/pdfs/{pdf_doc.id}/")
    }

@pdfRouter.get("/files", response=List[PdfSchema], auth=django_auth)
def list_pdfs(request):
    pdfs = PDFDocument.objects.all()
    return [
        {
            "id": pdf.id,
            "name": pdf.name,
            "content_url": request.build_absolute_uri(f"/api/upload/pdfs/{pdf.id}/")
        }
        for pdf in pdfs
    ]

@pdfRouter.get("/pdfs/{pdf_id}/", auth=None)
def get_pdf_content(request, pdf_id: int):
    pdf_doc = get_object_or_404(PDFDocument, id=pdf_id)
    response = HttpResponse(pdf_doc.file_content, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{pdf_doc.name or "document.pdf"}"'
    return response

@pdfRouter.delete("/pdfs/{pdf_id}/", response={204: None}, auth=django_auth)
def delete_pdf(request, pdf_id: int):
    pdf_doc = get_object_or_404(PDFDocument, id=pdf_id)
    pdf_doc.delete()
    return HttpResponse(status=204)