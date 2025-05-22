from django.db import IntegrityError
from dmsApp.models import Archive


class ArchiveService:
    @staticmethod
    def getArchives() -> Archive:
        return Archive.objects.all()

    def createArchive(self, _name) -> None:
        archive = Archive()
        archive.name = _name
        try:
            archive.save()
        except IntegrityError as e:
            raise IntegrityError(e)
