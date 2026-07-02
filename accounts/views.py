from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group

from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()

            if form.cleaned_data.get('is_editor'):
                group = Group.objects.get(name="Editor")
                user.groups.add(group)

            login(request, user)
            return redirect("books:book_list")
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "accounts/register.html", context)


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("books:book_list")
        else:
            messages.error(request, "Invalid Credentials!")
    return render(request, "accounts/login.html")


def logoutUser(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return redirect("books:book_list")
