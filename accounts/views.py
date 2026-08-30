from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def delete_account(request):

    error = None

    if request.method == "POST":

        password = request.POST.get("password")

        user = authenticate(
            username=request.user.username,
            password=password
        )

        if user is not None:

            request.user.delete()

            return redirect("home")

        error = "Incorrect password. Your account was not deleted."

    return render(
        request,
        "accounts/delete_account.html",
        {
            "error": error
        }
    )
def signup(request):

    if request.user.is_authenticated:

        return redirect("dashboard")

    if request.method == "POST":

        form = UserCreationForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            login(
                request,
                user
            )

            return redirect("dashboard")

    else:

        form = UserCreationForm()

    return render(
        request,
        "accounts/signup.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.user.is_authenticated:

        return redirect("dashboard")

    error = None

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(
                request,
                user
            )

            return redirect("dashboard")

        error = (
            "Invalid username or password."
        )

    return render(
        request,
        "accounts/login.html",
        {
            "error": error
        }
    )


def logout_view(request):

    logout(request)

    return redirect("home")