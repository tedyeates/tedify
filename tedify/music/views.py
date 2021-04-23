from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, View

from rest_framework import viewsets

from music.models import Genre, Artist
from music.serializers import GenreSerializer, ArtistSerializer
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
        print(request.POST)
        if "genre" not in request.POST:
            return HttpResponseNotFound('<h1>No genre selected</h1>')
        
        genre = request.POST.get("genre")
        print(genre)
        artists = Artist.objects.filter(genres__name=genre)
        return render(request, 'music/artists.html', {
            "artists": artists,
        })

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]