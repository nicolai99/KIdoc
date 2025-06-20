from django.db import transaction, IntegrityError

from dmsAPI.ProcessingError import ProcessingError
from dmsAPI.schema.ArchiveSchema import ArchiveSchema
from dmsApp.models import Archive, Attribute
from dmsApp.service.TypeService import TypeService


class ArchiveService:
    typeServive = TypeService()

    @staticmethod
    def getArchives() -> Archive:
        return Archive.objects.all()

    def getArchiveById(self, id: int) -> Archive:
        try:
            return Archive.objects.get(id=id)
        except Archive.DoesNotExist:
            raise ProcessingError("Archive does not exist", 1)

    def createArchive(self, archiveDTO: ArchiveSchema) -> None:
        _name = archiveDTO.name

        with transaction.atomic():
            archive = Archive(name=_name)
            self.saveArchive(archive)
            attributes = []
            for att in archiveDTO.attributes:
                type_obj = self.typeServive.getTypeById(att.type.id)
                attribute = Attribute(
                    archive=archive,
                    name=att.name,
                    label=att.label,
                    type=type_obj
                )
                attributes.append(attribute)
        Attribute.objects.bulk_create(attributes)

    def saveArchive(self, archive: Archive):
        try:
            archive.save()
        except IntegrityError:
            raise ProcessingError("Archivename already exists", 2)

    def editArchiveName(self, id, archiveDTO: ArchiveSchema):
        archive = self.getArchiveById(id)
        archive.name = archiveDTO.name
        self.saveArchive(archive)
