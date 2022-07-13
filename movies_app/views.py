from django.shortcuts import render, redirect
from .forms import GenreForm, MovieForm, CharacterForm
from .models import Character, Movie, Genre

# Create your views here.
def addGenre(requests):
    if requests.method == 'POST':
        form = GenreForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/Genres')
    else:
        form = GenreForm()

    return render(requests, 'movies/add_genre.html', context={'form':form})

def addMovie(requests):
    if requests.method == 'POST':
        form = MovieForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/Movies')
    else:
        form = MovieForm()

    return render(requests, 'movies/add_genre.html', context={'form':form})

def addCharacter(requests):
    if requests.method == 'POST':
        form = CharacterForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/Genres')
    else:
        form = CharacterForm()

    return render(requests, 'movies/add_genre.html', context={'form':form})

def genreList(requests):
    genres = Genre.objects.all 
    return render(requests, 'movies/genres.html', context={'genres':genres})

def movieList(requests):
    movies = Movie.objects.all 
    return render(requests, 'movies/movies.html', context={'movies':movies})

def characterList(requests):
    characters = Character.objects.all 
    return render(requests, 'movies/characters.html', context={'characters':characters})