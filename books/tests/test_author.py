from django.test import TestCase
from ..models import Author


class AuthorTest(TestCase):
    # Test Creation of Author
    def test_create_author(self):
        author = Author.objects.create(name="Test Author", most_famous_book="Test Book")
        self.assertEqual(author.name, "Test Author")
        self.assertEqual(Author.objects.count(), 1)
