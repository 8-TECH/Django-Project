from django.contrib import admin

# Register your models here.
from .models import Dates, Guidelines

admin.site.register(Dates)
admin.site.register(Guidelines)
