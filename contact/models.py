from django.db import models


class CollaborationRequest(models.Model):
    """ Stores a single collaboration form"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Collaboration request from {self.name}'
