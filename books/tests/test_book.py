from django.test import TestCase
from ..models import Book, Author, Genre
from ..forms import BookForm

class BookTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Author 1")
        self.genre = Genre.objects.create(name="Genre 1")

    # Test Creation of Books
    def test_create_book(self):
        book = Book.objects.create(
            title="Test Book",
            author=self.author,
            plot="Test Plot",
        )
        book.genres.add(self.genre)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(book.genres.count(), 1)


    # RELATION TEST
    def test_book_relations(self):
        book = Book.objects.create(
            title="Relation Book",
            author=self.author,
            plot="Test Plot",
        )

        book.genres.add(self.genre)
        self.assertIn(self.genre, book.genres.all())

        