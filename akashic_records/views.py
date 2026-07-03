from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse


def home(request):
    if request.method == "GET":
        return redirect(reverse("books:user_book_list"))
    return HttpResponse("<h1> Welcome to Home Page </h1>")
