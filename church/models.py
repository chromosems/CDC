from django.db import models


# Create your models here.
class Contact(models.Model):
    names = models.CharField(max_length=100)
    from_email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)


class DataFile(models.Model):
    data = models.FileField()

    def save(self, *args, **kwargs):
        super(DataFile, self).save(*args, **kwargs)
        filename = self.data.url
