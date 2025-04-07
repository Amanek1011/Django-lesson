from django.urls import path
<<<<<<< HEAD
from .views import hello, about, album
=======
from .views import hello
>>>>>>> da0b40f956e8dda35aa1370c65bc5b515daa0b13
from . import views

urlpatterns = [
    path('', hello, name='hello'),
<<<<<<< HEAD
    path('about', about, name='about'),
    path('album', album, name='album'),
    path('authors_list', views.authors_list, name='authors_list'),
    path('authors_list_2', views.AuthorsListView.as_view(), name='authors_list_2'),
=======
    path('author_list', views.authors_list, name = 'author_list'),
    path('author_list_2', views.authors_list, name = 'author_list_2'),
    path('song_list', views.songs_list, name = 'song_list'),
    path('song_list_2',views.songs_list, name = 'song_list_2')
>>>>>>> da0b40f956e8dda35aa1370c65bc5b515daa0b13
]