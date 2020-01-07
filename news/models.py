from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# DJANGO-ORM (Object relational mapping)


class News(models.Model):
    CATEGORIES = (("0", "Politics"), ("1", "Sports"), ("2", "Business"), ("3", "International"))
    title = models.CharField(max_length=255)
    content = models.TextField()
    count = models.IntegerField(default=0)
    category = models.CharField(max_length=2, choices=CATEGORIES)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to="news", null=True)
