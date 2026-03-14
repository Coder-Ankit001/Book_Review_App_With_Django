from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from django.db.models import Count

from .models import Author, Genre, Book
from .forms import AuthorForm, BookForm

""" Author Views """
class AuthorListView(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'authors/author_list.html'
    context_object_name = 'authors'
    login_url = '/accounts/login/'
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.annotate(books_count=Count('books'))

class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
    context_object_name = 'author'
    login_url = '/accounts/login/'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.object).prefetch_related('genres')
        return context

class AuthorCreateView(PermissionRequiredMixin, CreateView):
    model = Author
    template_name = 'authors/author_form.html'
    permission_required = 'books.add_author'
    form_class = AuthorForm

class AuthorUpdateView(PermissionRequiredMixin, UpdateView):
    model = Author
    template_name = 'authors/author_form.html'
    permission_required = 'books.change_author'
    form_class = AuthorForm

class AuthorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Author
    permission_required = 'books.delete_author'
    success_url = reverse_lazy('books:author_list')


""" Books Views """
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    login_url = '/accounts/login/'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.select_related('author').prefetch_related('genres')

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = '/accounts/login/'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().select_related('author').prefetch_related('genres')

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'books/book_form.html'
    permission_required = 'books.add_book'
    form_class = BookForm

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    permission_required = 'books.change_book'
    form_class = BookForm

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    permission_required = 'books.delete_book'
    success_url = reverse_lazy('books:book_list')


""" Genre Views """
class GenreListView(LoginRequiredMixin, ListView):
    model = Genre
    template_name = 'genres/genre_list.html'
    context_object_name = 'genres'
    login_url = '/accounts/login/'
    paginate_by = 10

    def get_queryset(self):
        return Genre.objects.annotate(books_count=Count('books')).order_by('name')
    
class GenreDetailView(LoginRequiredMixin, DetailView):
    model = Genre
    template_name = 'genres/genre_detail.html'
    context_object_name = 'genre'
    login_url = '/accounts/login/'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.filter(genres=self.object).prefetch_related('author')
        return context
    
class GenreCreateView(PermissionRequiredMixin, CreateView):
    model = Genre
    template_name = 'genres/genre_form.html'
    permission_required = 'books.add_genre'
    fields = ['name']

class GenreUpdateView(PermissionRequiredMixin, UpdateView):
    model = Genre
    template_name = 'genres/genre_form.html'
    permission_required = 'books.change_genre'
    fields = ['name']

class GenreDeleteView(PermissionRequiredMixin, DeleteView):
    model = Genre
    permission_required = 'books.delete_genre'
    success_url = reverse_lazy('books:genre_list')
