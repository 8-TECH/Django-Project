from django.contrib import admin

# Register your models here.
from .models import Scrol, Slide, News

admin.site.register(Scrol)
admin.site.register(Slide)
admin.site.register(News)

