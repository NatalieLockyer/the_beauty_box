from django.db import models

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=3000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video_url = models.URLField(max_length=3000, null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title