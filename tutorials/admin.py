from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tutorial

class TutorialAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'rating',
        'video',
        'video_url',
    )
    summernote_fields = (
        'description',
    )

    ordering = ('rating',)

admin.site.register(Tutorial, TutorialAdmin)