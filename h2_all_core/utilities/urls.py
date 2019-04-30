from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url('communication/', include('utilities.communication.urls'))
]
