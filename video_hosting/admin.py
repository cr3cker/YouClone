from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Description', {'fields': ['description']}),
        ('Video Preview', {'fields': ['image']}),
        ('Video File (mp4)', {'fields': ['file']}),
    ]
    list_display = ('title', 'file', 'create_at')
    list_filter = ['create_at']
    search_fields = ('title', 'file', 'image', 'create_at')


admin.site.register(Video, VideoAdmin)