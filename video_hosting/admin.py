from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'create_at')

admin.site.register(Video)
