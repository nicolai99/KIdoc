from typing import List

from django.http import HttpResponse
from dmsAPI.schema.ArchiveSchema import ArchiveSchema
from dmsApp.models import Archive
from dmsApp.service.ArchiveService import ArchiveService
from ninja import Router

archiveRouter = Router()


@archiveRouter.get("/", tags=["Archive"], summary="Get all archives", response=List[ArchiveSchema])
def getArchives(request):
    return Archive.objects.all()


@archiveRouter.post("/", tags=["Archive"], summary="Create a new archive", response={201: None})
def createArchive(request, archive: ArchiveSchema):
    service = ArchiveService()
    service.createArchive(_name=archive.name)
    return HttpResponse(201)
