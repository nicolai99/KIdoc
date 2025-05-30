from django.db import IntegrityError
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
