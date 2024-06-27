from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, 'Draft'), (1, 'Published'))

class Blog(models.Model):
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    image_url = models.URLField(max_length=3000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)