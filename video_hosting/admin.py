from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title and Description', {
            'fields': ('title', 'description')
        }),
        ('Preview and Video', {
            'classes': ('collapse',),
            'fields': ('image', 'file'),
        }),
    ]
    date_hierarchy = 'create_at'
    empty_value_display = '-empty-'
    list_display = ('title', 'file', 'create_at')
    list_filter = ['create_at']
    search_fields = ('title', 'file', 'image', 'create_at')


admin.site.register(Video, VideoAdmin)