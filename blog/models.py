from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20)
    datetime = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextField()
    coverImage = models.ImageField(upload_to='images')
    datetime = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
