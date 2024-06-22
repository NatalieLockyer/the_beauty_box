from django.contrib import admin
from .models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'rating',
        'video',
    )

    ordering = ('rating',)

admin.site.register(Tutorial, TutorialAdmin)