from django.db import models


# Create your models here.
class FileCnab(models.Model):
    file = models.FileField(upload_to="upload/")
