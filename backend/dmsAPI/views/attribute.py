from ninja import Router

from dmsAPI.schema.AttributesSchema import AttributesSchema
from dmsApp.service.AttributeService import AttributeService

attributeRouter = Router()


@attributeRouter.post("/", tags=["Attribute"], summary="Add Attribute")
def addAttribute(request, attributeDTO: AttributesSchema):
    attributeService = AttributeService()
    attributeService.add_attribute(attributeDTO)


@attributeRouter.delete("/{id}", tags=["Attribute"], summary="Delete Attribute")
def deleteAttribute(request, id: int):
    attributeService = AttributeService()
    attributeService.deleteAttribute(id)
