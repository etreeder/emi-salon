from django.urls import path
from . import views

app_name = "salonapp"
urlpatterns = [
    path("", views.Home, name="Home")
]
