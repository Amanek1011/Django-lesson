from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from apps.spotify.models import Author


def hello(request):
    return HttpResponse('Hello, world!')


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'spotify/authors_list.html', {'authors': authors})


class AuthorsListView(ListView):
    model = Author
    template_name = 'spotify/authors_list_2.html'
    context_object_name = 'authors'


def about(request):
    return render(request, 'about.html')

def album(request):
    authors = Author.objects.all()
    return render(request, 'album.html', {'authors': authors})

