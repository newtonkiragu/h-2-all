from django.conf.urls import url
from .views import CallbackHandler


urlpatterns = [
    url('callback/', CallbackHandler.as_view()),
]
