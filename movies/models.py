from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    star = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)