from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True)
    createOn = models.DateTimeField(auto_now_add=True)


class Archive(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Type(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Attribute(BaseModel):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="attributes")
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE, related_name="attributes")

    def __str__(self):
        return self.label


class PDFDocument(BaseModel):
    file = models.BinaryField()
    name = models.CharField(max_length=255)
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE, related_name="docs")

    def __str__(self):
        return f"PDF {self.id} - {self.file.name}"


class AttributesValue(BaseModel):
    pdf = models.ForeignKey(PDFDocument, on_delete=models.CASCADE, related_name="attribute_values")
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="values")
    value = models.TextField()

    def __str__(self):
        return f"{self.attribute.label}: {self.value}"
