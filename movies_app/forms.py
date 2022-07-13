from django.forms import ModelForm
from .models import Character, Movie, Genre

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre']

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'movie' ]

