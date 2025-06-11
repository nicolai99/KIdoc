import logging

from dmsAPI.schema.AttributesSchema import AttributesSchema
from dmsApp.models import Attribute
from dmsApp.service.ArchiveService import ArchiveService
from dmsApp.service.TypeService import TypeService

logger = logging.getLogger(__name__)


class AttributeService:
    typeService = TypeService()
    archiveService = ArchiveService()

    def add_attribute(self, attribute: AttributesSchema):
        archive = self.archiveService.getArchiveById(attribute.archive_id)
        type = self.typeService.getTypeById(attribute.type.id)
        try:
            Attribute.objects.create(name=attribute.name, label=attribute.label, type=type, archive=archive)
        except Exception:
            return False

    def deleteAttribute(self, id: int):
        attribute = Attribute.objects.get(id=id)
        attribute.delete()
