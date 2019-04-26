from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home),
    path('bh', views.borehole),
    path("price", views.price_list),
    path('newp', views.create_price),
    path('newbh', views.create_borehole)
]
