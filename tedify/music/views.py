from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, View

from rest_framework import viewsets

from music.models import Genre, Artist, Album
from music.serializers import GenreSerializer, ArtistSerializer, AlbumSerializer
from rest_framework import permissions


class GenreListView(ListView):
    model = Genre
    template_name = "music/genres.html"

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArtistView(View):
    def post(self, request, *args, **kwargs):
        # If no genre return 404
        if "genre" not in request.POST:
            return HttpResponseNotFound('<h1>No genre selected</h1>')
        
        genre = request.POST.get("genre")
        # Get artists by genre sent
        artists = Artist.objects.filter(genres__name=genre)
        return render(request, 'music/artists.html', {
            "artists": artists,
        })

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]


class AlbumView(View):
    def post(self, request, *args, **kwargs):
        # If no genre return 404
        if "artist" not in request.POST:
            return HttpResponseNotFound('<h1>No genre selected</h1>')
        
        artist = request.POST.get("artist")
        # Get albums by artist sent
        albums = Album.objects.filter(artists__name=artist)
        return render(request, 'music/albums.html', {
            "albums": albums,
        })

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]