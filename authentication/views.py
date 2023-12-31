from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from slack_integration.slack_service import send_message


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Hi {username}, your account was created successfully"
            )
            return redirect("home")
    else:
        form = UserRegisterForm()

    return render(request, "register.html", {"form": form})


@login_required()
def profile(request):
    return render(request, "profile.html")


def slack_integration(request):
    response = send_message('#general', 'Hello from Bliss!')
    return HttpResponse('Message sent successfully!')