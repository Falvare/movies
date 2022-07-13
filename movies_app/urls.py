from django.urls import path
from .views import addGenre, addCharacter, addMovie

urlpatterns = [
    path('add-genre/', addGenre, name='add genre'),
    path('add-movie/', addMovie, name='add movie'),
    path('add-character/', addCharacter, name='add character'),
]
