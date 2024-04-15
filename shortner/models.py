from django.db import models

# Create your models here.

class URL(models.Model):
    link = models.CharField(max_length=10000)
    short_link = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.link