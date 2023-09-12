# slack_integration/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('slack_integration/', views.slack_integration, name='slack_integration'),
]