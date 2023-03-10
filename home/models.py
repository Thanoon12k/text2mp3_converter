from django.db import models

class Converter(models.Model):
    text=models.CharField(max_length=1000)
    mp3=models.FileField(upload_to='media',null=True,blank=True)

    def __str__(self):
        return str(self.id)