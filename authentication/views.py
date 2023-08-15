import logging

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import HttpResponse, render

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration(request):
    logger.info("Registration view accessed.")
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            logger.info("Form is valid. Saving user.")
            user_form.save()
            logger.info("User saved successfully.")
            return HttpResponse("<h1>Registration successfully</h1>")
        else:
            logger.info("Form is invalid: %s", user_form.errors)
    else:
        user_form = UserCreationForm()
    return render(request, 'registration.html', {'user_form' : user_form})


def login(request):
    logger.info("Login view accessed.")
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info("User logged in: %s", username)
                return HttpResponse("<h1>Login successful</h1>")
            else:
                logger.info("Invalid login credentials for user: %s", username)
        else:
            logger.info("Login form is invalid: %s", login_form.errors)
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})