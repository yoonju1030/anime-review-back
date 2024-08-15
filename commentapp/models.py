from django.db import models

# Create your models here.
class Comment(models.Model):
    user_id = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    anime = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)