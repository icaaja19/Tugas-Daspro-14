# contoh di siteapp/models.py atau polls/models.py
from django.db import models

class Settings(models.Model):
    name = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.value}"
