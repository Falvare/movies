from django.urls import path
from .views import addGenre, addCharacter, addMovie, genreList, characterList, movieList, movieDetails

urlpatterns = [
    path('add-genre/', addGenre, name='add genre'),
    path('add-movie/', addMovie, name='add movie'),
    path('add-character/', addCharacter, name='add character'),
    path('genres/', genreList, name='genres'),
    path('', movieList, name='movies'),
    path('movies/', movieList, name='movies'),
    path('movie-details/<int:pk>', movieDetails, name='movie details'),
    path('characters/', characterList, name='characters'),
]
