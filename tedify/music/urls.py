from django.urls import path, include

from rest_framework import routers

from music.views import GenreListView

urlpatterns = [
    path('', GenreListView.as_view(), name='genres'),
]