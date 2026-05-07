from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q
from django.db.models import Count

from .models import Author, Genre, Book
from .forms import AuthorForm, BookForm

""" Author Views """


class AuthorListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "books.view_author"
    model = Author
    template_name = "dashboard/author_list.html"
    context_object_name = "authors"
    login_url = "/accounts/login/"
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.annotate(books_count=Count("books"))


class AuthorDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "books.view_author"
    model = Author
    template_name = "authors/author_detail.html"
    context_object_name = "author"
    login_url = "/accounts/login/"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.filter(author=self.object).prefetch_related(
            "genres"
        )
        return context


class AuthorCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "books.add_author"
    model = Author
    template_name = "authors/author_form.html"
    form_class = AuthorForm


class AuthorUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "books.change_author"
    model = Author
    template_name = "authors/author_form.html"
    form_class = AuthorForm


class AuthorDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "books.delete_author"
    model = Author
    success_url = reverse_lazy("books:author_list")


""" Books Views """


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "dashboard/book_list.html"
    context_object_name = "books"
    login_url = "/accounts/login/"
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.select_related("author").prefetch_related("genres")


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    login_url = "/accounts/login/"
    paginate_by = 10

    def get_queryset(self):
        return (
            super().get_queryset().select_related("author").prefetch_related("genres")
        )


class BookCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "books.add_book"
    model = Book
    template_name = "books/book_form.html"
    form_class = BookForm


class BookUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "books.change_book"
    model = Book
    template_name = "books/book_form.html"
    form_class = BookForm


class BookDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "books.delete_book"
    model = Book
    success_url = reverse_lazy("books:book_list")


def user_book_list(request):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 16)  # 16 books per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "books/book_list.html",
        {"is_paginated": True, "books": page_obj, "page_obj": page_obj},
    )


""" Genre Views """


class GenreListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "books.view_genre"
    model = Genre
    template_name = "dashboard/genre_list.html"
    context_object_name = "genres"
    login_url = "/accounts/login/"
    paginate_by = 10

    def get_queryset(self):
        return Genre.objects.annotate(books_count=Count("books")).order_by("name")


class GenreDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    permission_required = "books.view_genre"
    model = Genre
    template_name = "genres/genre_detail.html"
    context_object_name = "genre"
    login_url = "/accounts/login/"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.filter(genres=self.object).prefetch_related(
            "author"
        )
        return context


class GenreCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "books.add_genre"
    model = Genre
    template_name = "genres/genre_form.html"
    fields = ["name"]


class GenreUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "books.change_genre"
    model = Genre
    template_name = "genres/genre_form.html"
    fields = ["name"]


class GenreDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = "books.delete_genre"
    model = Genre
    success_url = reverse_lazy("books:genre_list")


def user_genre_list(request):
    genre_list = Genre.objects.annotate(books_count=Count("books")).order_by("name")
    paginator = Paginator(genre_list, 10)  # 10 books per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "genres/genre_list.html",
        {"is_paginated": True, "genres": page_obj, "page_obj": page_obj},
    )


""" Search Books"""


# Search with Keyword
def search_book(request):
    query = request.GET.get("q", "")
    books = Book.objects.filter(Q(title__icontains=query))
    paginator = Paginator(books, 16)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "books/book_list.html",
        {"is_paginated": True, "books": page_obj, "page_obj": page_obj},
    )


# Search Books with Genre
def search_book_genre(request, pk):
    books = Book.objects.filter(genres__id=pk).distinct()
    paginator = Paginator(books, 16)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "books/book_list.html",
        {"is_paginated": True, "books": page_obj, "page_obj": page_obj},
    )
