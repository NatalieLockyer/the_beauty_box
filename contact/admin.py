from django.contrib import admin
from .models import CollaborationRequest

# Register your models here.

@admin.register(CollaborationRequest)


class CollaborationRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)
