from django.test import TestCase
from django.urls import reverse

from music.models import Genre

class GenreListViewTest(TestCase):

    def test_page_access(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    
    def test_templates(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'music/genres.html')
        self.assertTemplateUsed(response, 'music/card_display.html')