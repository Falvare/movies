from django.urls import path
from .views import register, Login, profile

urlpatterns = [
    path('register/', register, name='register' ),
    path('login/', Login.as_view(), name='login' ),
    path('profile/', profile, name='profile' ),
]
