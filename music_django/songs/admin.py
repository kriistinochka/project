from django.contrib import admin

from . import models

admin.site.register(models.Category)
admin.site.register(models.Playlist)
admin.site.register(models.Genre)
admin.site.register(models.Song)
