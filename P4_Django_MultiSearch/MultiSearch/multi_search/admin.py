from django.contrib import admin

# Register your models here.

from multi_search import models

admin.site.register(models.Video)
admin.site.register(models.Classification)
admin.site.register(models.Direction)
