from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from apps.spotify.models import Author, Song


def hello(request):
    return HttpResponse('Hello, world!')


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'spotify/authors_list.html',{'authors': authors})

class AuthorsListView(ListView):
    model = Author
    template_name = 'spotify/authors_list_2.html'
    context_object_name = 'authors'

def songs_list(request):
    songs = Song.objects.all()
    return render(request,'spotify/songs_list.html',{'songs': songs})

class SongsListView(ListView):
    model = Song
    template_name = 'spotify/songs_list_2.html'
    context_object_name = 'songs'