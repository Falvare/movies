from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import GenreForm, MovieForm, CharacterForm
from .models import Character, Movie, Genre
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def addGenre(requests):
    if requests.method == 'POST':
        form = GenreForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('/genres')
    else:
        form = GenreForm()

    return render(requests, 'movies/add_genre.html', context={'form':form})

@login_required
def addMovie(requests):
    if requests.method == 'POST':
        form = MovieForm(requests.POST)
        if form.is_valid():

            movie = form.save(commit=False)
            movie.added_by = requests.user
            movie.save()

            # This will manually set the genre field to the choices checked in the form and then save the many to many field
            movie.genre.set(form.cleaned_data.get('genre'))
            form.save_m2m()

            return redirect('/movies')
    else:
        form = MovieForm()

    return render(requests, 'movies/add_genre.html', context={'form':form})

@login_required
def addCharacter(requests, pk):
    if requests.method == 'POST':
        form = CharacterForm(requests.POST)
        if form.is_valid():
            character = form.save(commit=False)
            character.added_by = requests.user
            character.movie = Movie.objects.get(pk=pk)
            character.save()
            return redirect('/characters')
    else:
        form = CharacterForm()

    return render(requests, 'movies/add_genre.html', context={'form':form})

def genreList(requests):
    genres = Genre.objects.all 
    return render(requests, 'movies/genres.html', context={'genres':genres})

def movieList(requests):
    movies = Movie.objects.all 
    return render(requests, 'movies/movies.html', context={'movies':movies})

def movieDetails(requests, pk):
    movie = Movie.objects.get(pk=pk)
    movie_characters = Character.objects.filter(movie=pk)

    context = {
        'movie':movie,
        'characters':movie_characters
    }

    return render(requests, 'movies/movie_details.html', context=context)

def characterList(requests):
    characters = Character.objects.all 
    return render(requests, 'movies/characters.html', context={'characters':characters})