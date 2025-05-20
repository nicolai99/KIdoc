from django.http import JsonResponse
from dmsApp.models import PDFDocument
from ninja import Router, UploadedFile, File, Path

pdfRouter = Router()

@pdfRouter.post("/upload")
def upload_pdf(request, file: UploadedFile = File(...)):
    if not file.name.endswith(".pdf"):
        return JsonResponse({"error": "Nur PDF-Dateien erlaubt."}, status=400)

    pdf = PDFDocument.objects.create(file=file)
    return {"message": "Upload erfolgreich", "id": pdf.id}

@pdfRouter.delete("/delete/{pdf_id}")
def delete_pdf(request, pdf_id: int = Path(...)):
    try:
        pdf = PDFDocument.objects.get(id=pdf_id)
        pdf.file.delete(save=False)  # Datei aus Storage löschen
        pdf.delete()                 # Datenbankeintrag löschen
        return {"message": "PDF erfolgreich gelöscht"}
    except PDFDocument.DoesNotExist:
        return JsonResponse({"error": "PDF nicht gefunden"}, status=404)
