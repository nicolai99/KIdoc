from dmsAPI.ProcessingError import ProcessingError
from dmsApp.models import Type


class TypeService:
    def getAllTypes(self):
        return Type.objects.all()
    
    def getTypeById(self, id):
        try:
            return Type.objects.get(id=id)
        except Type.DoesNotExist:
            raise ProcessingError("Type does not exist", 3)
