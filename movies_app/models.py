from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=10)

class Movie(models.Model):
    title = models.CharField(max_length=20, unique=True)
    genre = models.ManyToManyField(Genre)

class Character(models.Model):
    name = models.CharField(max_length=20)
    movies = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE)