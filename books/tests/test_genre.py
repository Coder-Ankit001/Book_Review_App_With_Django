from django.test import TestCase
from ..models import Genre


class GenreTest(TestCase):
    # Test Creation of Genre
    def test_create_author(self):
        genre = Genre.objects.create(name="Test Genre")
        self.assertEqual(genre.name, "Test Genre")
        self.assertEqual(Genre.objects.count(), 1)
