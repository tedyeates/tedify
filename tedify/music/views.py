from django.shortcuts import render
from django.views.generic import ListView
from music.models import Genre

# Create your views here.
class GenresListView(ListView):
    model = Genre
    template_name = "music/genres.html"