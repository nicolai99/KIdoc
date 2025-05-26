from typing import List

from django.http import HttpResponse
from dmsAPI.schema.TypeSchema import TypeSchema
from dmsApp.models import Type
from dmsApp.service.TypeService import TypeService
from ninja import Router

typeRouter = Router()


@typeRouter.get("/", tags=["Type"], summary="Get all types", response=List[TypeSchema])
def getTypes(request):
    return Type.objects.all()


@typeRouter.post("/", tags=["Type"], summary="Create a new type", response={201: None})
def createType(request, type: TypeSchema):
    service = TypeService()
    service.createType(_name=type.name)
    return HttpResponse(201)
