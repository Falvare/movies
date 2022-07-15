from django.urls import path
from .views import addGenre, addCharacter, addMovie, genreList, characterList, movieList, movieDetails, genreMovies, DeleteMovie, DeleteCharacter

urlpatterns = [
    path('add-genre/', addGenre, name='add genre'),
    path('add-movie/', addMovie, name='add movie'),
    path('genres/', genreList, name='genres'),
    path('genre/<int:pk>', genreMovies, name='genre details'),
    path('', movieList, name='movies'),
    path('movies/', movieList, name='movies'),
    path('movie-details/<int:pk>/', movieDetails, name='movie details'),
    path('movie-details/<int:pk>/add-character', addCharacter, name='add character'),
    path('characters/', characterList, name='characters'),
    path('delete-movie/<int:pk>', DeleteMovie.as_view(), name='delete movie'),
    path('delete-character/<int:pk>', DeleteCharacter.as_view(), name='delete character'),
]
