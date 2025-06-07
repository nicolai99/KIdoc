import json
import logging
import os

from google import genai

from dmsApp.models import Attribute
from dmsApp.service.ArchiveService import ArchiveService
from dmsApp.service.PdfService import PdfService

logger = logging.getLogger(__name__)


class GeminiService:
    client = None
    geminiFile = None
    question = None
    response = None
    attributes = None
    pdfService = PdfService()
    archiveService = ArchiveService()
    archiveName = None

    def connect(self):
        self.client = genai.Client(api_key=os.getenv("GOOGLEAPIKEY"))

    def uploadFile(self, url):
        self.geminiFile = self.client.files.upload(file=url)

    def generateQuestion(self, attributes):
        self.attributes = attributes

    def getAttributesByPdf(self, pdfId: int):
        pdf = self.pdfService.getPdfById(pdfId)
        archive = self.archiveService.getArchiveById(pdf.archive_id)
        self.archiveName = archive.name
        attributes = Attribute.objects.prefetch_related("type").filter(archive=archive)
        self.attributes = []
        for att in attributes:
            value = {"attribut": att.name, "type": att.type.name}
            self.attributes.append(value)
        self.attributes = json.dumps(self.attributes)
        self.generateContent()
        return self.response.text

    def generateContent(self):
        self.response = self.client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=[f"In diesem Doc nach attributen suchen", self.attributes, self.geminiFile,
                      """antworte nur in einer kommaseparierten liste (Datum im dd.mm.yyyy) format ohne zeilenumbruch value1,value2""",
                      ]
        )
