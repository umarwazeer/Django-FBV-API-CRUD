from django.db import models


# Create your models here.
class Patient(models.Model):
    objects = None
    name = models.CharField(max_length=225)
    contact = models.IntegerField(unique=True)
    location = models.CharField(max_length=225)

    def __str__(self):
        return self.name + ' ' + str(self.contact) + ' ' + self.location

