from django.test import TestCase
from ..models import Author
from ..forms import AuthorForm

class AuthorTest(TestCase):

    # Test Creation of Author
    def test_create_author(self):
        author = Author.objects.create(
            name="Test Author",
            most_famous_book="Test Book"
        )
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.first().name, "Test Author")


class AuthorFormTest(TestCase):

    # Author Form Validation
    def test_validate_author_form(self):
        
        form1 = AuthorForm({
            "name": "Test Author",
            "most_famous_book": "Test Book"
        })

        form2 = AuthorForm({
            "most_famous_book": "Test Book"
        })

        self.assertTrue(form1.is_valid())
        self.assertFalse(form2.is_valid())