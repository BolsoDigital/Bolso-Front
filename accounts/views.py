from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import CustomUserCreationForm, CustomAuthenticationForm


def register_view(request):
    if request.method == "POST":
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else:
        user_form = CustomUserCreationForm()

    return render(request, "register.html", {"user_form": user_form})


def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("bolsoDigital:expenses_list")
    else:
        form = CustomAuthenticationForm()

    return render(request, "login.html", {"login_form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
