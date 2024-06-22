from django.db import models

from profiles.models import UserProfile


import datetime

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """ Stores a single Beauty-Blog post """
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='blog_posts', default='1')
    content = models.TextField(default='1')
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=3000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Orders the Beauty-Blogs from newest to oldest creation time
        """
        ordering = ["created_on"]

    def __str__(self):
        return f" {self.title}"


class Comment(models.Model):
    """ Stores a single comment entry """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
