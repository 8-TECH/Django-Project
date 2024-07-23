from django.db import models

# Create your models here.

class Faith(models.Model):
    religion = models.CharField(max_length=200)
    short_form = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.religion
