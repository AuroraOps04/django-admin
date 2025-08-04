from django.db import models

# Create your models here.

class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    md5 = models.CharField(max_length=32)
    mimetype = models.CharField(max_length=50)
    size = models.PositiveIntegerField()
    upload_time = models.DateTimeField(auto_now_add=True)
    original_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file.name