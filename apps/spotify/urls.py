from django.urls import path
from .views import hello
from . import views

urlpatterns = [
    path('', hello, name='hello'),
    path('author_list', views.authors_list, name = 'author_list'),
    path('author_list_2', views.authors_list, name = 'author_list_2'),
    path('song_list', views.songs_list, name = 'song_list'),
    path('song_list_2',views.songs_list, name = 'song_list_2')
]