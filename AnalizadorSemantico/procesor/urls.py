from django.conf.urls import url
from . import views

# home.
urlpatterns = [
    url('', views.home)
]
