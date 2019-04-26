from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home),
    path('bh', views.borehole),
    path("price", views.create_fie),
]
