from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple
from .models import Character, Movie, Genre

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['genre']

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'genre']

    def __init__(self, *args, **kwargs):
    
        super(MovieForm, self).__init__(*args, **kwargs)
        
        self.fields["genre"].widget = CheckboxSelectMultiple()
        self.fields["genre"].queryset = Genre.objects.all()


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name' ]

