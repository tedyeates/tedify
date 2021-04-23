from django.test import TestCase
from music.models import *
class ModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Genre.objects.create(name='Horror', description='adwada')
        Artist.objects.create(name='Ted', age="12", description='adwada')
        Album.objects.create(name='ScarySong', description='adwada')

    def test_genre_name(self):
        genre = Genre.objects.all()[0]
        self.assertEqual(genre.name, str(genre))

    def test_artist_name(self):
        artist = Artist.objects.all()[0]
        self.assertEqual(artist.name, str(artist))

    def test_genre_name(self):
        album = Album.objects.all()[0]
        self.assertEqual(album.name, str(album))