from django.db import models

# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length=256)
    Last_Name = models.CharField(max_length=256)
    Email = models.EmailField()

    def __str__(self):
        return self.First_Name
