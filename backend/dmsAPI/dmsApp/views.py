from ninja import Router, File
from ninja.files import UploadedFile
from django.http import JsonResponse
from .models import PDFDocument

router = Router()

@router.post("/upload")
def upload_pdf(request, file: UploadedFile = File(...)):
    if not file.name.endswith(".pdf"):
        return JsonResponse({"error": "Nur PDF-Dateien erlaubt."}, status=400)

    pdf = PDFDocument.objects.create(file=file)
    return {"message": "Upload erfolgreich", "id": pdf.id}
