from django.urls import path
from . import views

urlpatterns = [path("", views.aircraft_search, name="search")]