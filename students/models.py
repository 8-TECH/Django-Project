from django.db import models

# Create your models here.

class Dates(models.Model):
    dateName = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)
    units = models.CharField(max_length=100, null=True, blank=True)
    cat1 = models.CharField(max_length=100, null=True, blank=True)
    cat2 = models.CharField(max_length=100, null=True, blank=True)
    examstart = models.CharField(max_length=100, null=True, blank=True)
    examend = models.CharField(max_length=100, default=0)
    
    def __str__(self):
        return self.dateName 
    
class Guidelines(models.Model):
    guideline = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.guideline 