from django.db import models

# Create your models here.

class ListItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField()
    def __str__(self):
        return self.name
    class Admin:
        pass
