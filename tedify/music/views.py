from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import viewsets

from music.models import Genre
from music.serializers import GenreSerializer
from rest_framework import permissions

class GenreListView(ListView):
    model = Genre
    template_name = "music/genres.html"


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]