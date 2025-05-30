from typing import List

from ninja import Router

from dmsAPI.schema.TypeSchema import TypeSchema
from dmsApp.models import Type

typeRouter = Router()


@typeRouter.get("/", tags=["Type"], summary="Get all Types", response={200: List[TypeSchema]})
def getAllTypes(request):
    return Type.objects.all()
