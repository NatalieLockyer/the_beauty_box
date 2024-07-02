from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'content',
        'image_url',
        'image',
        'rating',
        'created_on',
        'status',
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