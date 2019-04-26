from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path("", views.home),
    url('bh/(?P<borehole_id>\d+)$', views.borehole),
    path("price", views.price_list),
    path('newp', views.create_price),
    url('newbh/(?P<borehole_id>\d+)?$', views.create_borehole)
]
