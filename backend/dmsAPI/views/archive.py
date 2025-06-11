from typing import List

from django.http import HttpResponse, Http404
from ninja import Router

from dmsAPI.schema.ArchiveSchema import ArchiveSchema
from dmsApp.models import Archive
from dmsApp.service.ArchiveService import ArchiveService

archiveRouter = Router()


@archiveRouter.get("/", tags=["Archive"], summary="Get all archives", response=List[ArchiveSchema])
def getArchives(request):
    return Archive.objects.all()


@archiveRouter.post("/", tags=["Archive"], summary="Create a new archive", response={201: None})
def createArchive(request, archiveDTO: ArchiveSchema):
    service = ArchiveService()
    service.createArchive(archiveDTO)
    return HttpResponse(201)


@archiveRouter.put("/edit/{id}", tags=["Archive"], summary="Edit archive name", response={200: None})
def editArchiveName(request, id: int, archiveDTO: ArchiveSchema):
    service = ArchiveService()
    service.editArchiveName(id, archiveDTO)
    return HttpResponse(200)


@archiveRouter.get("/{archive_id}", tags=["Archive"], summary="Get archive by ID", response=ArchiveSchema)
def getArchiveById(request, archive_id: int):
    try:
        archive = Archive.objects.prefetch_related('attributes__type').get(id=archive_id)
        return archive
    except Archive.DoesNotExist:
        raise Http404("Archive not found")
