from django.db import models


# Create your models here.

class FileModel(models.Model):
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return str(self.id)
