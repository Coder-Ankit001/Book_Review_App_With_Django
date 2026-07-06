from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    most_famous_book = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("books:author_detail", kwargs={"pk": self.pk})


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("books:genre_list")


class Book(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genres = models.ManyToManyField(Genre, related_name="books")
    featured_image = models.ImageField(
        upload_to="media/book_images/", null=True, blank=True
    )
    plot = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("books:book_detail", kwargs={"pk": self.pk})
