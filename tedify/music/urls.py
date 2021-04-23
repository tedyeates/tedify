from django.urls import path
from music.views import GenresListView

urlpatterns = [
    path('', GenresListView.as_view(), name='genres')
]