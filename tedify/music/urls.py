from django.urls import path, include

from rest_framework import routers

from music.views import GenreListView, ArtistView, AlbumView

urlpatterns = [
    path('', GenreListView.as_view(), name='genres'),
    path('artist/', ArtistView.as_view(), name='artists'),
    path('album/', AlbumView.as_view(), name='albums')
]