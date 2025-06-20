from django.db import IntegrityError

from dmsAPI.ProcessingError import ProcessingError
from dmsApp.models import Type


class TypeService:
    @staticmethod
    def getTypes() -> Type:
        return Type.objects.all()

    def createType(self, _name) -> None:
        type = Type()
        type.name = _name
        try:
            type.save()
        except IntegrityError as e:
            raise IntegrityError(e)

    def getTypeById(self, id):
        try:
            return Type.objects.get(id=id)
        except Type.DoesNotExist:
            raise ProcessingError("Type does not exist", 1)
