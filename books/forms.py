from django import forms
from .models import Author, Book, Genre

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'most_famous_book']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Author full name'
            }),
            'most_famous_book': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Most recognized work'
            }),
        }
        labels = {
            'most_famous_book': 'Most Famous Book',
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres', 'featured_image', 'plot']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Author full name'
            }),
            'author': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Most recognized work'
            }),
            'genres': forms.NumberInput(attrs={
                'class': 'input-field',
                'min': 1
            }),
            'featured_image': forms.ClearableFileInput(attrs={
                'class': 'file-input',
            }),
            'plot': forms.Textarea(attrs={
                'class': 'input-field',
            }),
        }
        labels = {
            'featured_image': 'Featured Image',
        }


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name', 'most_famous_book', 'books_written']
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'input-field',
#                 'placeholder': 'Author full name'
#             }),
#             'most_famous_book': forms.TextInput(attrs={
#                 'class': 'input-field',
#                 'placeholder': 'Most recognized work'
#             }),
#             'books_written': forms.NumberInput(attrs={
#                 'class': 'input-field',
#                 'min': 1
#             }),
#         }
#         labels = {
#             'most_famous_book': 'Most Famous Book',
#             'books_written': 'Number of Books Written',
#         }