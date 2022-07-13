from django.db import models

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.genre

class Movie(models.Model):
    title = models.CharField(max_length=20, unique=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=20)
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name