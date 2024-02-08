from django.db import models

# Create your models here.
class Post(models.Model):
    postTitle = models.CharField(max_length=50)
    postContent = models.CharField(max_length=1000)