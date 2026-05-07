from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    # Authors Endpoints
    path("dahsboard/authors/", views.AuthorListView.as_view(), name="author_list"),
    path("authors/create/", views.AuthorCreateView.as_view(), name="author_create"),
    path(
        "authors/update/<int:pk>/",
        views.AuthorUpdateView.as_view(),
        name="author_update",
    ),
    path(
        "authors/detail/<int:pk>/",
        views.AuthorDetailView.as_view(),
        name="author_detail",
    ),
    path(
        "authors/delete/<int:pk>/",
        views.AuthorDeleteView.as_view(),
        name="author_delete",
    ),
    # Books Endpoints
    path("books/", views.user_book_list, name="user_book_list"),
    path("dashboard/books/", views.BookListView.as_view(), name="book_list"),
    path("books/create/", views.BookCreateView.as_view(), name="book_create"),
    path("books/update/<int:pk>/", views.BookUpdateView.as_view(), name="book_update"),
    path("books/detail/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("books/delete/<int:pk>/", views.BookDeleteView.as_view(), name="book_delete"),
    # Genres Endpoints
    path("genres/", views.user_genre_list, name="user_genre_list"),
    path("dashboard/genres/", views.GenreListView.as_view(), name="genre_list"),
    path("genres/create/", views.GenreCreateView.as_view(), name="genre_create"),
    path(
        "genres/update/<int:pk>/", views.GenreUpdateView.as_view(), name="genre_update"
    ),
    path(
        "genres/detail/<int:pk>/", views.GenreDetailView.as_view(), name="genre_detail"
    ),
    path(
        "genres/delete/<int:pk>/", views.GenreDeleteView.as_view(), name="genre_delete"
    ),
    # Search Boks
    path("search/", views.search_book, name="search_book"),
    path("search/genre/<int:pk>/", views.search_book_genre, name="search_book_genre"),
]
