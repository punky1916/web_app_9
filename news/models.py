from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# DJANGO-ORM (Object relational mapping)


class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    count = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, null=True)
    category = models.ManyToManyField(Category, related_name="news_categoreis")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to="news", null=True)

    def get_absolute_url(self):
        return reverse("single_news", kwargs={"pk": self.pk, "slug": self.slug})

