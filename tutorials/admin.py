from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'rating',
        'description',
        'video',
        'video_url',
    )

    ordering = ('rating',)

admin.site.register(Tutorial, TutorialAdmin)