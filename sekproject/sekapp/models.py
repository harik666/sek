from django.db import models


# Create your models here.


class Persons(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    designation = models.TextField()

    def __str__(self):
        return self.name
