# tableDetail/urls.py

from django.urls import path
from tableDetail import views

urlpatterns = [
    path("", views.table_index, name='table_index'),
    path("<int:pk>/", views.table_detail, name="table_detail"),
]