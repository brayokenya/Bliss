from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
import logging

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