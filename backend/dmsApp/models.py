from django.db import models

# Create your models here.
class PDFDocument(models.Model):
    file = models.FileField(upload_to="pdfs/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PDF {self.id} - {self.file.name}"


class Archive(models.Model):
    name = models.CharField(max_length=255)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255)
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Doc(models.Model):
    url = models.BinaryField()  # Binary oder FileField?
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="docs")
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE, related_name="docs")
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Doc {self.id}"


class Attribute(models.Model):
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="attributes")
    archive = models.ForeignKey(Archive, on_delete=models.CASCADE, related_name="attributes")
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label


class AttributesValue(models.Model):
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE, related_name="attribute_values")
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="values")
    value = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.attribute.label}: {self.value}"
