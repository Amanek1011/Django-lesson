from django.contrib import admin

# Register your models here.

from apps.spotify.models import *

# admin.site.register(Author)
# admin.site.register(Song)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'album_count')
    list_display_links = ('name','surname', 'album_count')
    list_filter = ('name', 'surname', 'album_count')
    search_fields = ('name', 'surname')
    ordering = ('id', 'name', 'surname')

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'name')
    list_display_links = ('id', 'author', 'name')
    list_filter = ('id', 'author', 'name')
    search_fields = ('id', 'author', 'name')
    ordering = ('id', 'author', 'name')