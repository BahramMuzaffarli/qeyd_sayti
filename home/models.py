from django.db import models

# Create your models here.
from django.db import models

class Note(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    note = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
