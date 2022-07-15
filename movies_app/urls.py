from django.urls import path
from .views import addGenre, addCharacter, addMovie, genreList, characterList, movieList, movieDetails

urlpatterns = [
    path('add-genre/', addGenre, name='add genre'),
    path('add-movie/', addMovie, name='add movie'),
    path('genres/', genreList, name='genres'),
    path('', movieList, name='movies'),
    path('movies/', movieList, name='movies'),
    path('movie-details/<int:pk>/', movieDetails, name='movie details'),
    path('movie-details/<int:pk>/add-character', addCharacter, name='add character'),
    path('characters/', characterList, name='characters'),
]
