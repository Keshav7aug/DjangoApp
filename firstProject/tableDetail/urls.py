# tableDetail/urls.py

from django.urls import path
from tableDetail import views

urlpatterns = [
    path("", views.home, name='home'),
]