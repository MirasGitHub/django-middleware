from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, default='name')
    surname = models.CharField(max_length=100, default='surname')


class Book(models.Model):
    title = models.CharField(max_length=100, default='title')
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, default='genre')
