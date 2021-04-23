from music.models import Artist, Genre
import random

def random_genres():
    genres = list(Genre.objects.all())
    for artist in Artist.objects.all():
        print(random.sample(genres, 3))
        random_samples = random.sample(genres, 3)
        artist.genres.add(*random_samples)
