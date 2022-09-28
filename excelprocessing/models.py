from django.db import models

class XlsxFileModel(models.Model):
    file = models.FileField('Файл', upload_to='uploads/')