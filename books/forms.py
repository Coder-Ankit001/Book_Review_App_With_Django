from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "most_famous_book"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input-field", "placeholder": "Author full name"}
            ),
            "most_famous_book": forms.TextInput(
                attrs={"class": "input-field", "placeholder": "Most recognized work"}
            ),
        }
        labels = {
            "most_famous_book": "Most Famous Book",
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "genres", "featured_image", "plot"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "input-field", "placeholder": "Author full name"}
            ),
            "author": forms.Select(attrs={"class": "input-field"}),
            "genres": forms.Select(
                attrs={
                    "class": "input-field",
                }
            ),
            "featured_image": forms.ClearableFileInput(
                attrs={
                    "class": "file-input",
                }
            ),
            "plot": forms.Textarea(
                attrs={
                    "class": "input-field",
                }
            ),
        }
        labels = {
            "featured_image": "Featured Image",
        }
