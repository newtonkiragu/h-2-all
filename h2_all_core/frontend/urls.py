from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home),
    path("price", views.create_fie),
]
