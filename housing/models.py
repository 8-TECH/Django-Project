from django.db import models

# Create your models here.

class House(models.Model):
    house_image = models.ImageField(default="default.jpeg")
    house_name = models.CharField(max_length=100)
    house_type = models.CharField(max_length=100, null=True, blank=True)
    rent = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.house_name
    
