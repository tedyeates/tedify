from music.models import Artist, Genre, Album
import random

def random_data():
    """Attach 3 random objects to many to many field"""
    genres = list(Genre.objects.all())
    for artist in Artist.objects.all():
        random_samples = random.sample(genres, 3)
        artist.genres.add(*random_samples)
    
    artists = list(Artist.objects.all())
    for album in Album.objects.all():
        random_samples = random.sample(artists, 3)
        album.artists.add(*random_samples)
