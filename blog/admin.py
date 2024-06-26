from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Comment


class BlogAdmin(SummernoteModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'image_url',
        'image',
        'rating',
        'created_on',
        'status',
    )
    summernote_fields = (
        'content',
    )

    ordering = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'body',
        'approved',
    )


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)