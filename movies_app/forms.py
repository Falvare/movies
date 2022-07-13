from django.forms import ModelForm

class GenreForm(ModelForm):
    class Meta:
        fields = ['genre']

class MovieForm(ModelForm):
    class Meta:
        fields = ['title', 'genre']

class CharacterForm(ModelForm):
    class Meta:
        fields = ['name', 'movie' ]

