from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

<<<<<<< HEAD
from apps.spotify.models import Author
=======
from apps.spotify.models import Author, Song
>>>>>>> da0b40f956e8dda35aa1370c65bc5b515daa0b13


def hello(request):
    return HttpResponse('Hello, world!')


def authors_list(request):
    authors = Author.objects.all()
<<<<<<< HEAD
    return render(request, 'spotify/authors_list.html', {'authors': authors})

=======
    return render(request, 'spotify/authors_list.html',{'authors': authors})
>>>>>>> da0b40f956e8dda35aa1370c65bc5b515daa0b13

class AuthorsListView(ListView):
    model = Author
    template_name = 'spotify/authors_list_2.html'
    context_object_name = 'authors'

<<<<<<< HEAD

def about(request):
    return render(request, 'about.html')

def album(request):
    authors = Author.objects.all()
    return render(request, 'album.html', {'authors': authors})

=======
def songs_list(request):
    songs = Song.objects.all()
    return render(request,'spotify/songs_list.html',{'songs': songs})

class SongsListView(ListView):
    model = Song
    template_name = 'spotify/songs_list_2.html'
    context_object_name = 'songs'
>>>>>>> da0b40f956e8dda35aa1370c65bc5b515daa0b13
