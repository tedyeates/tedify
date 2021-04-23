from django.urls import path, include

from rest_framework import routers

from music.views import GenreListView, ArtistView

urlpatterns = [
    path('', GenreListView.as_view(), name='genres'),
    path('artist/', ArtistView.as_view(), name='artists')
]